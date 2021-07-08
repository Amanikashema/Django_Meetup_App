from django.contrib import admin

from .models import Meetup, Location, Participant


# Register your models here.


class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')  # to add as columns in admin area
    list_filter = ('location', 'date')  # functionality to filter
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)
