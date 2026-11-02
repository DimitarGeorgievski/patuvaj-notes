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