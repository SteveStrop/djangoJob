from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import datetime
from EstateAgent import Scrapers
from django.views import generic

from jobs.forms import JobForm
from jobs.models import Job, Vendor, Client, Agent


# Create your views here.

def job_form(request, pk):
    """
    View for displaying a JobDetailView for editing will become the default and maybe make JobDetailView
    redundant
    """
    job = get_object_or_404(Job, pk=pk)
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = JobForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model appointment field)
            job.appointment = form.cleaned_data['appointment']
            job.floorplan = form.cleaned_data['floorplan']
            job.photos = form.cleaned_data['photos']
            job.ref = form.cleaned_data['ref']
            job.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('index'))

    # If this is a GET (or any other method) create the default form using field from forms.JobForm
    else:
        appointment = job.appointment
        floorplan = job.floorplan
        photos = job.photos
        ref = job.ref
        form = JobForm(
                initial={
                        'ref':         ref,
                        'appointment': appointment,
                        'floorplan':   floorplan,
                        'photos':      photos
                })

    context = {
            'form': form,
            'job':  job,
    }

    return render(request, 'jobs/job_form.html', context)


def test_create(request):
    def get_client(candidate):
        try:
            return Client.objects.filter(name__contains=candidate.client)[0]
        except IndexError:
            return Client.objects.create(name=candidate.client)

    def get_agent(candidate):
        try:
            agent = Agent.objects.filter(branch__contains=candidate.agent)[0]
            # print(f'candidate.agent = {candidate.agent}. agent = {agent} at try')
            # input("Continue?")
        except IndexError:
            agent = Agent.objects.create(branch=candidate.agent)
            # print(f'candidate.agent = {candidate.agent}. agent = {agent} at except')
            # input("Continue?")
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

    def scrape(scraper):
        jobs_links = scraper.extract_job_links()
        jobs = [scraper.extract_job(l) for l in jobs_links]
        scraper.scraper_close()
        return jobs

    candidate_jobs = scrape(Scrapers.KaScraper()) + scrape(Scrapers.HsScraper())
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
                    phone=candidate.vendor.phone_1 if candidate.vendor.phone_1 else 'N/A',
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
