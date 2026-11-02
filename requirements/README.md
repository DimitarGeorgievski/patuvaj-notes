Requirements and acceptance criteria for Patuvaj.

## Question 5 — Preventing Double-Booking

The system must not allow more travellers to book a departure than the available capacity, even when multiple travellers attempt to book the last available place at the same time.

## Lab 3.2 — Gherkin

### Question 6

I added the values 0, 1, 11, 12, and 13. Zero checks that an empty group is refused, while 1 checks the minimum valid group size. Values 11 and 12 test the upper boundary, and 13 checks that a group above the maximum is refused. These boundary values help reveal errors that normal group sizes might miss.