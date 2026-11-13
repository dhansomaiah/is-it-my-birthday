from datetime import date, timedelta

from birthday import is_it_my_birthday


def accuracy(month, day):
    """Ask every day for 400 years, for someone born on this date."""
    today, end, right, days = date(2000, 1, 1), date(2400, 1, 1), 0, 0
    while today < end:
        really = (today.month, today.day) == (month, day)
        right += is_it_my_birthday() == really
        days += 1
        today += timedelta(days=1)
    return 100 * right / days


def test_right_almost_every_day():
    assert round(accuracy(7, 14), 1) == 99.7


def test_even_better_for_leap_day_babies():
    assert round(accuracy(2, 29), 1) == 99.9
