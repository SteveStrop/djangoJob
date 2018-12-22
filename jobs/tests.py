from datetime import datetime

from django.test import TestCase

# Create your tests here.
from .models import Job, Client, Agent, Appointment, Address, Vendor


class AddressModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Address.objects.create(street='22 Inverewe Place, Westcroft, Milton Keynes', postcode='MK4 4FY')

    def setUp(self):
        global address
        address = Address.objects.get(pk=1)

    def test__str__(self):
        self.assertEqual('22 Inverewe Place, Westcroft, Milton Keynes, MK4 4FY', str(address))


class AppointmentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Appointment.objects.create(date=datetime(2018, 12, 29, 13, 30))

    def setUp(self):
        global appointment
        appointment = Appointment.objects.get(pk=1)

    def test__str__(self):
        self.assertEqual(f'{appointment.date.strftime("%a %d %b %H: %M")}', str(appointment))


class ClientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Client.objects.create(name_1='Key Agent')

    def setUp(self):
        global client
        client = Client.objects.get(pk=1)

    def test__str__(self):
        self.assertEqual('Key Agent', str(client))


class VendorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Vendor.objects.create(name_1='Mrs Josephine Blogs')

    def setUp(self):
        global vendor
        vendor = Vendor.objects.get(pk=1)

    def test__str__(self):
        self.assertEqual('Mrs Josephine Blogs', str(vendor))


class AgentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Address.objects.create(street='1, The High St, Stony Stratford, Milton Keynes', postcode='MK11 1GH')
        Agent.objects.create(branch='Connells - Stony Stratford', address=Address.objects.get(pk=1))

    def setUp(self):
        global agent
        agent = Agent.objects.get(pk=1)

    def test__str__(self):
        self.assertEqual('Connells - Stony Stratford', str(agent))


class JobModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Address.objects.create(street='1, The High St, Stony Stratford, Milton Keynes', postcode='MK11 1GH')
        Agent.objects.create(branch='Connells - Stony Stratford', address=Address.objects.get(pk=1))
        Vendor.objects.create(name_1='Mrs Josephine Blogs')
        Client.objects.create(name_1='Key Agent')
        Appointment.objects.create(date=datetime(2018, 12, 29, 13, 30))
        Job.objects.create(
                ref='HIP 1000000001',
                client=Client.objects.get(pk=1),
                agent=Agent.objects.get(pk=1),
                vendor=Vendor.objects.get(pk=1),
                appointment=Appointment.objects.get(pk=1),
                property_type='House',
                beds=2,
                floorplan=True,
        )

    def setUp(self):
        global job
        job = Job.objects.get(pk=1)

    def test__str__(self):
        self.assertEqual('HIP 1000000001', str(job))
