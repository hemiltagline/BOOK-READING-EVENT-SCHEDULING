from django.contrib import admin
from events.models import Event, EventListingsInCity, ProductListingsInEvent, Ticket

admin.site.register(Event)
admin.site.register(EventListingsInCity)
admin.site.register(ProductListingsInEvent)
admin.site.register(Ticket)
