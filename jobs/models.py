from django.db import models

# Create your models here.
from django.urls import reverse


class Client(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200, null=True, blank=True)
    postcode = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class ClientDetail(models.Model):
    phone = models.CharField(max_length=13)
    name = models.CharField(max_length=13, null=True, blank=True)
    email = models.CharField(max_length=13, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Agent(models.Model):
    branch = models.CharField(max_length=500)
    address = models.CharField(max_length=200, null=True, blank=True)
    postcode = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return str(self.branch)


class AgentDetail(models.Model):
    phone = models.CharField(max_length=13)
    name = models.CharField(max_length=13, null=True, blank=True)
    email = models.CharField(max_length=13, null=True, blank=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# class Client(models.Model):
#     name_1 = models.CharField(max_length=100, verbose_name='name')
#     name_2 = models.CharField(max_length=100, verbose_name='name', null=True, blank=True)
#     phone_1 = models.CharField(max_length=13, verbose_name='phone', null=True, blank=True)
#     phone_2 = models.CharField(max_length=13, verbose_name='phone', null=True, blank=True)
#     phone_3 = models.CharField(max_length=13, verbose_name='phone', null=True, blank=True)
#     notes = models.TextField(null=True, blank=True)
#
#     def __str__(self):
#         return str(self.name_1)
#
#
# class Agent(models.Model):
#     branch = models.CharField(max_length=100, verbose_name='branch')
#     name_1 = models.CharField(max_length=100, verbose_name='name', null=True, blank=True)
#     name_2 = models.CharField(max_length=100, verbose_name='name', null=True, blank=True)
#     phone_1 = models.CharField(max_length=13, verbose_name='phone', null=True, blank=True)
#     phone_2 = models.CharField(max_length=13, verbose_name='phone', null=True, blank=True)
#     phone_3 = models.CharField(max_length=13, verbose_name='phone', null=True, blank=True)
#     notes = models.TextField(null=True, blank=True)
#     address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, blank=True)
#
#     @property
#     def get_branch(self):
#         return self.branch
#
#     def __str__(self):
#         return str(self.branch)


class Job(models.Model):
    ref = models.CharField(max_length=13)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200)
    postcode = models.CharField(max_length=8, null=True, blank=True)
    PROPERTY_CHOICE = (
            ('house', 'house'),
            ('flat', 'flat'),
            ('bungalow', 'bungalow'),
            ('semi', 'semi')
    )
    property_type = models.CharField(max_length=20, choices=PROPERTY_CHOICE, null=True, blank=True)
    beds = models.SmallIntegerField(default=3, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    floorplan = models.BooleanField(default=True, verbose_name='Floorplan required')
    photos = models.SmallIntegerField(default=20)
    folder = models.CharField(max_length=100, null=True, blank=True)
    specific_reqs = models.TextField(default='Streetscape: 1', null=True, blank=True)
    status = models.BooleanField(default=True, verbose_name='Active')
    history = models.TextField(null=True, blank=True)
    appointment = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['appointment']

    def get_absolute_url(self):
        """Return the url to access a detailed record for this job"""
        return reverse("job-detail", args=[str(self.id)])

    def __str__(self):
        return str(self.ref)


class Vendor(models.Model):
    phone = models.CharField(max_length=13)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.name) if self.name else ""
