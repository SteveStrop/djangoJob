from django.db import models
from django.contrib.postgres.fields import JSONField


# Create your models here.

class Client(models.Model):
    name_1 = models.CharField(max_length=100, verbose_name='name')
    name_2 = models.CharField(max_length=100, verbose_name='name', null=True, blank=True)
    phone_1 = models.CharField(max_length=13, verbose_name='phone', null=True, blank=True)
    phone_2 = models.CharField(max_length=13, verbose_name='phone', null=True, blank=True)
    phone_3 = models.CharField(max_length=13, verbose_name='phone', null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name_1)


class Agent(models.Model):
    branch = models.CharField(max_length=100, verbose_name='branch')
    name_1 = models.CharField(max_length=100, verbose_name='name', null=True, blank=True)
    name_2 = models.CharField(max_length=100, verbose_name='name', null=True, blank=True)
    phone_1 = models.CharField(max_length=13, verbose_name='phone', null=True, blank=True)
    phone_2 = models.CharField(max_length=13, verbose_name='phone', null=True, blank=True)
    phone_3 = models.CharField(max_length=13, verbose_name='phone', null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def get_branch(self):
        return self.branch

    def __str__(self):
        return str(self.branch)


class Job(models.Model):
    ref = models.CharField(max_length=13)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, blank=True)
    property_type = models.CharField(max_length=20, null=True, blank=True)
    beds = models.SmallIntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    floorplan = models.BooleanField(default=True, verbose_name='Floorplan required')
    photos = models.SmallIntegerField(default=20)
    folder = models.CharField(max_length=100, null=True, blank=True)
    specific_reqs = models.TextField(default='Streetscape : 1', null=True, blank=True)
    status = models.BooleanField(default=True, verbose_name='Active')
    history = models.TextField(null=True, blank=True)
    appointment = JSONField()

    def __str__(self):
        return str(self.ref)


class Address(models.Model):
    street = models.CharField(max_length=200)
    postcode = models.CharField(max_length=8)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Address"

    def __str__(self):
        return f'{self.street}, {self.postcode}'


# class Appointment(models.Model):
#     date = models.DateTimeField(unique=True)
#     job = models.ForeignKey(Job, on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name_plural = "Appointment"
#
#     def __str__(self):
#         return str(self.date.strftime("%a %d %b %H: %M"))


class Vendor(models.Model):
    name_1 = models.CharField(max_length=100, verbose_name='name')
    name_2 = models.CharField(max_length=100, verbose_name='name', null=True, blank=True)
    phone_1 = models.CharField(max_length=13, verbose_name='phone', null=True, blank=True)
    phone_2 = models.CharField(max_length=13, verbose_name='phone', null=True, blank=True)
    phone_3 = models.CharField(max_length=13, verbose_name='phone', null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name_1)
