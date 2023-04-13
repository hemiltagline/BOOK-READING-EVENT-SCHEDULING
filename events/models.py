from django.db import models
from users.models import User
from books.models import Book
from cities.models import CitiesPage
from books.models import Product
from backend.models import BaseModel
from django.core.exceptions import ValidationError


class Event(BaseModel):
    CREATED = "created"
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

    STATUSES = (
        (CREATED, "Created"),
        (ACTIVE, "Active"),
        (COMPLETED, "Completed"),
        (CANCELLED, "Cancelled"),
    )

    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="events")
    city = models.ForeignKey(
        CitiesPage, on_delete=models.CASCADE, related_name="city_event"
    )
    address = models.CharField(max_length=500)
    description = models.TextField(max_length=1000, null=True, blank=True)
    start_time = models.DateTimeField()
    total_tickets = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUSES, default=CREATED)

    def __str__(self):
        return f"{self.book.title} event at {self.address} in {self.city.city_name}"


class EventListingsInCity(BaseModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    city = models.ForeignKey(CitiesPage, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.event.book.title} event in {self.city.city_name}"


class ProductListingsInEvent(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} in {self.event.book.title} event"


class Ticket(BaseModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="ticket")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_ticket"
    )
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        # Calculate the total number of sold tickets for the event
        sold_tickets = (
            self.event.ticket.aggregate(total_sold=models.Sum("quantity"))["total_sold"]
            or 0
        )

        # Calculate the total number of available tickets for the event
        available_tickets = self.event.total_tickets - sold_tickets

        # If the requested quantity of tickets exceeds the available tickets, raise a validation error
        if self.quantity > available_tickets:
            raise ValidationError("Not enough tickets available for this event")

    def save(self, *args, **kwargs):
        # Call the clean method to perform the validation check
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} ticket for {self.event.book.title}"
