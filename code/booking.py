"""
Patuvaj booking rule.

check_booking returns None when a booking is allowed,
or a short reason string when it must be refused.
"""


def check_booking(group_size, departure, remaining, cancelled, now):
    if not isinstance(group_size, int) or isinstance(group_size, bool):
        return "invalid group size"
    if group_size < 1 or group_size >= 12:
        return "group size must be between 1 and 12"
    if cancelled:
        return "departure cancelled for weather"
    if departure < now:
        return "departure is in the past"
    if remaining < group_size:
        return "not enough places left"
    return None