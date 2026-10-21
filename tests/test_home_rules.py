import sys
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from home_rules import (  # noqa: E402
    evaluate_climate,
    evaluate_security,
    load_events,
    process_events,
)


def test_evaluate_climate():
    assert evaluate_climate(26.0) == "turn_on_cooling"
    assert evaluate_climate(16.5) == "turn_on_heating"
    assert evaluate_climate(22.0) == "keep_climate"
    assert evaluate_climate(25.0) == "keep_climate"
    assert evaluate_climate(18.0) == "keep_climate"


def test_evaluate_security():
    assert evaluate_security("open", "away") == "send_door_warning"
    assert evaluate_security("open", "auto") == "security_ok"
    assert evaluate_security("closed", "away") == "security_ok"


def test_process_events():
    events = [
        {"room": "hall", "temperature": 22.0, "door": "open", "mode": "away"},
        {"room": "bedroom", "temperature": 26.0, "door": "closed", "mode": "auto"},
    ]

    assert process_events(events) == [
        {
            "room": "hall",
            "climate_action": "keep_climate",
            "security_action": "send_door_warning",
        },
        {
            "room": "bedroom",
            "climate_action": "turn_on_cooling",
            "security_action": "security_ok",
        },
    ]


def test_process_project_csv():
    path = Path(__file__).resolve().parents[1] / "data" / "smart_home_events_raw.csv"
    events = load_events(str(path))
    results = process_events(events)

    assert len(events) >= 20
    assert len(results) == len(events)
    assert results[0] == {
        "room": "living_room",
        "climate_action": "keep_climate",
        "security_action": "security_ok",
    }
    assert results[10]["climate_action"] == "turn_on_cooling"
    assert results[15]["climate_action"] == "turn_on_heating"
    assert results[8]["security_action"] == "send_door_warning"
