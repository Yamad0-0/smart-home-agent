# Отчёт по занятию 6. Функции и модуль правил агента умного дома

**Направление:** Умный дом
**Проект:** ООП-прототип агента умного дома
**Дата:** 21.10.2026

## Цель работы
Вынести повторяющуюся логику реакции агента в функции и подготовить модуль, который далее можно использовать в классах.

## Входные данные
События датчиков из `data/smart_home_events_raw.csv`:
`timestamp`, `room`, `temperature`, `light_lux`, `motion`, `door`, `mode`.

Пороги реакции агента:
- `HOT_TEMPERATURE = 25.0` — выше порога включается охлаждение;
- `COLD_TEMPERATURE = 18.0` — ниже порога включается обогрев;
- дверь `open` при режиме `away` — предупреждение безопасности.

## Что сделано
- Создан модуль `src/home_rules.py`:
  - `evaluate_climate()` — оценка климата;
  - `evaluate_security()` — оценка безопасности;
  - `process_event()` — обработка одного события;
  - `process_events()` — обработка списка событий;
  - `load_events()` — чтение событий из CSV.
- Добавлены тесты `tests/test_home_rules.py`.
- Проверка через `assert` встроена в демонстрационный запуск модуля.

## Результат
Команда `python src/home_rules.py` выводит:

```text
{'room': 'hall', 'climate_action': 'keep_climate', 'security_action': 'send_door_warning'}
{'room': 'bedroom', 'climate_action': 'turn_on_cooling', 'security_action': 'security_ok'}
Функции агента проверены
```

Проверка тестами:

```text
python -m pytest tests/ -v
5 passed
```

## Git
Изменения зафиксированы коммитом с сообщением:
`Занятие 6: модуль правил агента умного дома и тесты`
