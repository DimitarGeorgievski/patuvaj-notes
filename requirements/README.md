Requirements and acceptance criteria for Patuvaj.

## Question 5 — Preventing Double-Booking

The system must not allow more travellers to book a departure than the available capacity, even when multiple travellers attempt to book the last available place at the same time.

## Lab 3.2 — Gherkin

### Question 6

I added the values 0, 1, 11, 12, and 13. Zero checks that an empty group is refused, while 1 checks the minimum valid group size. Values 11 and 12 test the upper boundary, and 13 checks that a group above the maximum is refused. These boundary values help reveal errors that normal group sizes might miss.


## Lab 5.3 — Booking Rule and Automated Tests

### Question 11

The test `test_group_of_twelve_is_accepted` failed because the
code incorrectly refused groups of exactly 12 people. The condition
used `>= 12` instead of `> 12`.

Testing normal groups of three or four people would not reveal
the bug because those group sizes are below the maximum limit.

### Question 12

No. These tests call `check_booking` directly and test one booking
at a time. They cannot detect two simultaneous requests booking
the same remaining places.

A concurrent integration test would be needed. It should send two
booking requests at the same time when only one place remains
and verify that only one booking succeeds. This tests whether
the reservation operation is atomic.

## Lab 5.6 — PortSwigger Web Security Academy

### Question 13

Sofia should be able to see her own booking. The operator should
also be able to see bookings needed to manage departures, and the
assigned guide should only see the booking information needed for
the assigned trip.

I would write an authorization integration test where another
traveller tries to access Sofia's booking using its ID. The request
must be rejected with a 403 Forbidden or 404 Not Found response.
I would also verify that Sofia can access her own booking.