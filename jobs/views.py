from django.http import HttpResponse
from EstateAgent import Scrapers
from django.views import generic
from jobs.models import Job, Vendor, Client, Agent


# Create your views here.

def get_client(candidate):
    try:
        return Client.objects.filter(name__contains=candidate.client)[0]
    except IndexError:
        return Client.objects.create(name=candidate.client)


def get_agent(candidate):
    try:
        agent = Agent.objects.filter(branch__contains=candidate.agent)[0]
    except IndexError:
        agent = Agent.objects.create(branch=candidate.agent)
    return agent


def get_notes(candidate):
    try:
        note = '\n'.join(note for note in candidate.notes)
    except TypeError:
        note = ""
    return note


def get_history(candidate):
    try:
        note = '\n'.join(note for note in candidate.system_notes[0])
    except (TypeError, IndexError):
        note = ""
    return note


def test_create(request):
    k = Scrapers.KaScraper()
    jobs_links = k.extract_job_links()
    candidate_jobs = [k.extract_job(l) for l in jobs_links]
    k.scraper_close()
    for candidate in candidate_jobs:

        if Job.objects.all().filter(ref__contains=candidate.ref):
            pass
        else:
            job = Job.objects.create(
                    ref=candidate.ref,
                    client=get_client(candidate),
                    agent=get_agent(candidate),
                    address=candidate.appointment.address.street,
                    postcode=candidate.appointment.address.postcode,
                    appointment=candidate.appointment.date,
                    property_type=candidate.property_type,
                    beds=candidate.beds,
                    notes=get_notes(candidate),
                    floorplan=candidate.floorplan,
                    photos=candidate.photos,
                    folder=candidate.folder,
                    status=candidate.status,
                    history=get_history(candidate),
            )
            Vendor.objects.create(
                    name=candidate.vendor.name_1,
                    phone=candidate.vendor.phone_1,
                    # todo missing vendor notes (they're in Classes.Vendor but not in models.Vendor??)
                    job=job

            )

    return HttpResponse(f'{Job.objects.all().count()} jobs processed.\nStatus: OK.')


class IndexListView(generic.ListView):
    model = Job


class JobDetailView(generic.DetailView):
    model = Job

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(JobDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all Vendors
        context['vendor_list'] = Vendor.objects.all()
        return context
