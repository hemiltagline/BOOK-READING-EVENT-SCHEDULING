from django.contrib import admin
from events.models import Event, EventListingsInCity, ProductListingsInEvent

admin.site.register(Event)
admin.site.register(EventListingsInCity)
admin.site.register(ProductListingsInEvent)
