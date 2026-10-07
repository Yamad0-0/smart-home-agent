"""Заглушка будущего ООП-агента. Будет реализован в следующем проектном часе."""

class SensorEvent:
    def __init__(self, timestamp: str, room: str, temperature: float,
                 light_lux: int, motion: int, door: str, mode: str):
        self.timestamp = timestamp
        self.room = room
        self.temperature = temperature
        self.light_lux = light_lux
        self.motion = motion
        self.door = door
        self.mode = mode

class SmartHomeAgent:
    """Прототип: правила будут добавлены позже."""
    def decide(self, event: SensorEvent) -> str:
        if event.door == "open" and event.mode == "away":
            return "alarm: door open in away mode"
        if event.motion == 0 and event.light_lux > 50:
            return "turn_off_light"
        if event.temperature > 25.0:
            return "cool_down"
        if event.temperature < 18.0:
            return "heat_up"
        return "do_nothing"
