from datetime import datetime
from django.db import models
from django.forms import Textarea, TextInput
from django.contrib import admin
from .models import Agent, AgentDetail, Job, Vendor, Client, ClientDetail

# Register your models here.

admin.site.site_header = 'Estate Agent'


# admin.site.register(Vendor)


# admin.site.register(Job)


# admin.site.register(Agent)
# admin.site.register(Client)

class VendorInline(admin.TabularInline):
    model = Vendor
    extra = 1
    max_num = 3


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('phone', 'name', 'email')


# class AddressInline(admin.TabularInline):
#     model = Address
#     extra = 1
#     max_num = 1
#     fields = ('street', 'postcode')


# class AppointmentInline(admin.TabularInline):
#     model = Appointment
#     extra = 1
#     max_num = 1
#     fields = ('date',)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('ref', 'photos', 'floorplan')
    inlines = [VendorInline]


class AgentDetailsInline(admin.TabularInline):
    model = AgentDetail
    extra = 0


class ClientDetailsInline(admin.TabularInline):
    model = ClientDetail
    extra = 0


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    inlines = [AgentDetailsInline]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    inlines = [ClientDetailsInline]
