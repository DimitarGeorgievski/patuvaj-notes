## Lab 4.1 — Class and Sequence Diagrams

### Question 7

The word "atomic" means that checking the available places and reserving them happen as one indivisible operation.

This is important because two travellers might try to book the last available places at the same time. Without an atomic operation, both requests could see the same available places and both bookings could be confirmed, causing a double-booking. With an atomic operation, only one request can successfully reserve the places.

## Lab 4.2 — C4 Diagrams

### Question 8

Marko's guide app may display previously downloaded information, such as assigned trips and traveller details, while offline.

It must never confirm bookings or modify the remaining places for a departure without a network connection. Only the Booking Service can update the remaining places, ensuring that double-booking is prevented.

On the container diagram, this decision is shown in the Guide App description: it can display cached information offline, while the Booking Service is responsible for booking operations and availability updates.

## Question 9

Observer would genuinely help when a departure is cancelled due to bad weather. The Booking Service can notify affected travellers, guides and operators through separate subscribers without being tightly coupled to each of them.

Adding a design pattern would be over-engineering for a simple booking validation that has only one implementation. A regular method in the Booking Service is simpler and easier to maintain today.