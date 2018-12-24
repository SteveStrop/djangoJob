from datetime import datetime
from django.db import models
from django.forms import Textarea, TextInput
from django.contrib import admin
from .models import Client, Job, Agent, Address, Vendor  # Appointment Job2, Client2, Vendor2

# Register your models here.

admin.site.site_header = 'Estate Agent'
admin.site.register(Agent)
admin.site.register(Client)


class VendorInline(admin.TabularInline):
    model = Vendor
    extra = 1
    max_num = 1
    fields = ('name_1', 'phone_1', 'email', 'name_2', 'phone_2', 'phone_3')
    # show_change_link = True


class AddressInline(admin.TabularInline):
    model = Address
    extra = 1
    max_num = 1
    fields = ('street', 'postcode')


# class AppointmentInline(admin.TabularInline):
#     model = Appointment
#     extra = 1
#     max_num = 1
#     fields = ('date',)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['ref', 'get_address', 'get_agent_branch', 'get_appointment', 'photos', 'floorplan']
    inlines = [VendorInline, AddressInline] # , AppointmentInline]
    formfield_overrides = {
            models.CharField: {'widget': TextInput(attrs={'size': '20'})},
            models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 80})},
    }

    def get_agent_branch(self, obj):
        try:
            branch = obj.agent.branch
        except AttributeError:
            branch = ""
        return branch

    get_agent_branch.admin_order_field = 'agent'
    get_agent_branch.short_description = 'branch'

    def get_address(self, obj):
        try:
            address = obj.address_set.all()[0]
        except IndexError:
            address = ""
        return address

    get_address.short_description = "address"

    def get_appointment(self, obj):
        try:
            appointment = obj.appointment_set.all()[0]
        except IndexError:
            appointment = ""
        return appointment

    get_appointment.short_description = "appointment"
