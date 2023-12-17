# Tixguru - Event Ticketing System

Tixguru is a robust event ticketing system developed with Django, Python, and JavaScript. It provides a comprehensive platform for managing events, booking tickets, and engaging with a dynamic user community.

## Features

- **Event Management:** Organizers can effortlessly create, update, and manage events through a user-friendly interface.
- **Ticket Booking:** Users can easily browse and book tickets for a variety of events, ensuring a seamless booking experience.
- **Authentication:** Secure user authentication using Django REST Framework's Token-based authentication ensures data privacy and access control.
- **Event Discovery:** Explore a diverse range of events with a responsive and intuitive interface.
- **Payment Integration:** Secure payment processing guarantees a smooth and secure transaction experience for users.

## Getting Started

### Prerequisites

Ensure the following software is installed:

- Python (>=3.6)
- Django (>=3.0)
- Django REST framework (>=3.11)

### API Endpoints

# List all events

/events/ (GET)

# Get event details

/events/<event_id>/ (GET)

# Create a new event

/events/create/ (POST)

# Delete an event

/events/<event_id>/delete/ (DELETE)

# Update an event

/events/<event_id>/update/ (POST)
