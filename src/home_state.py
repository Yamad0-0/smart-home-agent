"""Состояние агента умного дома на базовых структурах данных."""

import csv
from pathlib import Path

THRESHOLDS = {
    "temperature": {"hot": 25.0, "cold": 18.0},
    "light": {"dark": 50, "bright": 300},
    "security": {"door_state": "open", "mode": "away"},
}

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "smart_home_events_raw.csv"

with DATA_PATH.open(encoding="utf-8", newline="") as file:
    raw_events = list(csv.DictReader(file))

events = [
    {
        "room": row["room"],
        "temperature": float(row["temperature"]),
        "light_lux": int(row["light_lux"]),
        "motion": int(row["motion"]),
        "door": row["door"],
        "mode": row["mode"],
        "light_state": (
            "bright"
            if int(row["light_lux"]) >= THRESHOLDS["light"]["bright"]
            else "dark"
            if int(row["light_lux"]) <= THRESHOLDS["light"]["dark"]
            else "normal"
        ),
    }
    for row in raw_events
]

decisions = []

for event in events:
    if event["temperature"] > THRESHOLDS["temperature"]["hot"]:
        climate_action = "turn_on_cooling"
    elif event["temperature"] < THRESHOLDS["temperature"]["cold"]:
        climate_action = "turn_on_heating"
    else:
        climate_action = "keep_climate"

    if (
        event["door"] == THRESHOLDS["security"]["door_state"]
        and event["mode"] == THRESHOLDS["security"]["mode"]
    ):
        security_action = "send_door_warning"
    else:
        security_action = "security_ok"

    decisions.append(
        {
            "room": event["room"],
            "climate_action": climate_action,
            "security_action": security_action,
        }
    )

print("Решения агента умного дома:")
for decision in decisions:
    print(decision)

assert len(decisions) == len(events)
assert decisions[0] == {
    "room": "living_room",
    "climate_action": "keep_climate",
    "security_action": "security_ok",
}
assert decisions[8] == {
    "room": "bedroom",
    "climate_action": "keep_climate",
    "security_action": "send_door_warning",
}
assert decisions[10] == {
    "room": "kitchen",
    "climate_action": "turn_on_cooling",
    "security_action": "security_ok",
}
assert decisions[15] == {
    "room": "living_room",
    "climate_action": "turn_on_heating",
    "security_action": "security_ok",
}
assert decisions[16] == {
    "room": "kitchen",
    "climate_action": "turn_on_heating",
    "security_action": "send_door_warning",
}
assert sum(event["light_state"] == "bright" for event in events) == 7
print("Проверка базовых структур пройдена")
