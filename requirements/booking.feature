Feature: Booking a departure

  Scenario: A group that fits is accepted
    Given the Matka kayak departure tomorrow at 09:00 has 6 places left
    When Sofia books it for 4 people
    Then the booking is confirmed
    And the departure has 2 places left

  Scenario: A group that is too large is refused
    Given a departure tomorrow with 20 places left
    When a traveller books it for 13 people
    Then the booking is refused

  Scenario: A departure cancelled for weather cannot be booked
    Given the Matka kayak departure tomorrow at 09:00 has been cancelled for weather
    When Sofia tries to book it for 2 people
    Then the booking is refused

  Scenario Outline: Group size limits
    Given a departure tomorrow with 20 places left
    When a traveller books it for <size> people
    Then the booking is <result>

    Examples:
      | size | result   |
      | 0    | refused  |
      | 1    | accepted |
      | 11   | accepted |
      | 12   | accepted |
      | 13   | refused  |