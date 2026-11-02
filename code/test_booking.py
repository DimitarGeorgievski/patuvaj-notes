from datetime import datetime, timedelta
from booking import check_booking

NOW = datetime(2027, 6, 1, 9, 0)
TOMORROW = NOW + timedelta(days=1)
def test_group_of_one_is_accepted():
    assert check_booking(
        1, TOMORROW, remaining=10, cancelled=False, now=NOW
    ) is None

def test_group_of_zero_is_refused():
    assert check_booking(
        0, TOMORROW, remaining=10, cancelled=False, now=NOW
    ) is not None
def test_group_of_eleven_is_accepted():
    assert check_booking(
        11, TOMORROW, remaining=15, cancelled=False, now=NOW
    ) is None
def test_group_of_twelve_is_accepted():
    assert check_booking(
        12, TOMORROW, remaining=15, cancelled=False, now=NOW
    ) is None
def test_group_of_thirteen_is_refused():
    assert check_booking(
        13, TOMORROW, remaining=15, cancelled=False, now=NOW
    ) is not None
def test_exactly_enough_places_are_accepted():
    assert check_booking(
        5, TOMORROW, remaining=5, cancelled=False, now=NOW
    ) is None
def test_one_place_short_is_refused():
    assert check_booking(
        5, TOMORROW, remaining=4, cancelled=False, now=NOW
    ) == "not enough places left"
def test_weather_cancelled_departure_is_refused():
    assert check_booking(
        2, TOMORROW, remaining=10, cancelled=True, now=NOW
    ) == "departure cancelled for weather"
def test_departure_in_the_past_is_refused():
    yesterday = NOW - timedelta(days=1)
    assert check_booking(
        2, yesterday, remaining=10, cancelled=False, now=NOW
    ) == "departure is in the past"
def test_non_integer_group_size_is_refused():
    assert check_booking(
        "5", TOMORROW, remaining=10, cancelled=False, now=NOW
    ) == "invalid group size"
def test_boolean_group_size_is_refused():
    assert check_booking(
        True, TOMORROW, remaining=10, cancelled=False, now=NOW
    ) == "invalid group size"