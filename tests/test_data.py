import csv
import os

def test_csv_exists_and_header():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "smart_home_events_raw.csv")
    path = os.path.abspath(path)
    assert os.path.exists(path), "Нет файла smart_home_events_raw.csv"
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames == ["timestamp", "room", "temperature", "light_lux", "motion", "door", "mode"]
        rows = list(reader)
        assert len(rows) >= 20, "Нужно минимум 20 строк данных"
