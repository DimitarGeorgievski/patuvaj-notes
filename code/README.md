Source code and automated tests for Patuvaj.

# Lab 5.3 — Patuvaj Booking Rule

The bug was in the maximum group size validation.

The condition used `group_size >= 12`, which incorrectly refused
bookings for exactly 12 people. The correct condition is
`group_size > 12`, because groups of up to 12 people are allowed.

The test `test_group_of_twelve_is_accepted` found the bug.

A test with a group of 5 people would not have found it because
5 is below the maximum limit, so the incorrect condition would
still allow that booking.