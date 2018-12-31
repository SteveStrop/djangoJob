from datetime import datetime
from django.db import models
from django.forms import Textarea, TextInput
from django.contrib import admin
from .models import Agent, AgentDetail, Job, Vendor, Client, ClientDetail

# Register your models here.

admin.site.site_header = 'Estate Agent'


class VendorInline(admin.TabularInline):
    model = Vendor
    extra = 1
    max_num = 3


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('phone', 'name', 'email')


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    inlines = [VendorInline]
    list_display = ('ref', 'client', 'agent', 'postcode', 'photos', 'floorplan','appointment')
    fieldsets = [
            ('Order:', {
                    'fields':
                        [
                                'ref',
                                ('client', 'agent')
                        ]
            }),
            ('Details:', {
                    'fields': [
                            # put vendor inline here
                            ('floorplan', 'photos'),
                            ('address', 'postcode'),
                            ('property_type', 'beds'),
                            'specific_reqs',
                            'notes',
                    ]
            }),
            ('Appointment:', {
                    'fields': [
                            'appointment',
                    ]
            }),
            ('History:', {
                    'fields': [
                            'history',
                    ]
            }),
    ]


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
