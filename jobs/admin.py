from datetime import datetime

from django.contrib import admin
from .models import Client, Job, Appointment, Agent, Address, Vendor


# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['ref', 'address', 'appointment', 'floorplan', 'photos']

admin.site.register(Address)
admin.site.register(Client)
admin.site.register(Appointment)
admin.site.register(Agent)
admin.site.register(Vendor)

