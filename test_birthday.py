from datetime import date, timedelta

import birthday


def live_with_it(tmp_path, monkeypatch, month, day):
    """Ask every day for 400 years, and correct it whenever it is wrong on the day."""
    monkeypatch.setattr(birthday, "MEMORY", tmp_path / "birthday.txt")
    today, end, wrong = date(2000, 1, 1), date(2400, 1, 1), 0
    while today < end:
        really = (today.month, today.day) == (month, day)
        if birthday.is_it_my_birthday(today) != really:
            wrong += 1
            birthday.it_is_actually(today)
        today += timedelta(days=1)
    return wrong


def test_wrong_exactly_once_in_400_years(tmp_path, monkeypatch):
    assert live_with_it(tmp_path, monkeypatch, 7, 14) == 1


def test_also_once_for_leap_day_babies(tmp_path, monkeypatch):
    assert live_with_it(tmp_path, monkeypatch, 2, 29) == 1
