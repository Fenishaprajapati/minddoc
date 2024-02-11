from django.contrib import admin

# Register your models here.
from .models import Record
from .models import Venue
from .models import Event
from .models import MindDocEventUser
from .models import QuizSubmissions, Appointments

admin.site.register(Record)
admin.site.register(QuizSubmissions)
admin.site.register(Appointments)
# admin.site.register(Venue)
# admin.site.register(Event)
admin.site.register(MindDocEventUser)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display=('name', 'address',)
    ordering=('name',)
    search_fields=('name', 'address','zip_code', 'phone', 'web', 'email_address')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields=(('name', 'venue'), 'event_date', 'description','manager')#kind of layout
    list_display=('name', 'event_date', 'venue')
    list_filter=('event_date', 'venue',)
    ordering=('-event_date',)
