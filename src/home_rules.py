"""Правила агента умного дома: климат, безопасность и обработка событий."""

import csv

HOT_TEMPERATURE = 25.0
COLD_TEMPERATURE = 18.0


def evaluate_climate(temperature: float) -> str:
    """Оценить температуру и выбрать действие климата."""
    if temperature > HOT_TEMPERATURE:
        return "turn_on_cooling"
    if temperature < COLD_TEMPERATURE:
        return "turn_on_heating"
    return "keep_climate"


def evaluate_security(door: str, mode: str) -> str:
    """Оценить состояние двери и режим контроллера."""
    if door == "open" and mode == "away":
        return "send_door_warning"
    return "security_ok"


def process_event(event: dict) -> dict:
    """Обработать одно событие датчиков."""
    return {
        "room": event["room"],
        "climate_action": evaluate_climate(float(event["temperature"])),
        "security_action": evaluate_security(str(event["door"]), str(event["mode"])),
    }


def process_events(events: list[dict]) -> list[dict]:
    """Обработать список событий и вернуть решения агента."""
    return [process_event(event) for event in events]


def load_events(path: str) -> list[dict]:
    """Прочитать события из CSV и привести значения к нужным типам."""
    with open(path, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return [
            {
                "timestamp": row["timestamp"],
                "room": row["room"],
                "temperature": float(row["temperature"]),
                "light_lux": int(row["light_lux"]),
                "motion": int(row["motion"]),
                "door": row["door"],
                "mode": row["mode"],
            }
            for row in reader
        ]


def _demo() -> None:
    events = [
        {"room": "hall", "temperature": 22.0, "door": "open", "mode": "away"},
        {"room": "bedroom", "temperature": 26.0, "door": "closed", "mode": "auto"},
    ]
    expected = [
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

    results = process_events(events)
    for result in results:
        print(result)

    assert results == expected
    print("Функции агента проверены")


if __name__ == "__main__":
    _demo()
