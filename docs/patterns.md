
# Lab 4.3 — Design Patterns

## 1. Observer Pattern

Observer would genuinely help when a departure is cancelled due to bad weather.

The Booking Service could publish a departure-cancelled event, and different subscribers could react to it. For example, the notification service could inform affected travellers, while the operator and guide could receive updates.

This avoids tightly coupling the Booking Service to every notification or update component.

## 2. Strategy Pattern

Strategy could help if Patuvaj supports multiple payment methods, such as card payments and bank transfers.

Each payment method could have its own strategy implementing the same interface. The Booking Service would use the selected strategy without containing all payment-processing logic itself.

This makes it easier to add another payment method without changing the existing booking logic.

## 3. Over-engineering

Using the Strategy pattern for a simple booking validation that has only one implementation would be over-engineering.

Creating separate strategy classes and interfaces for a single, unchanging validation algorithm would add unnecessary complexity. A simple method inside the Booking Service is better today.
