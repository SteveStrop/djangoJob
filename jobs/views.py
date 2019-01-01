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
        print(f'Candidate.agent is: {candidate.agent} \n agent is {agent}')
        input("Continue from try?")
    except IndexError:
        agent = Agent.objects.create(branch=candidate.agent)
        print(f'Candidate.agent is : {candidate.agent} \n agent is {agent}')
        input("Continue from except?")
    return agent


def test_create(request):
    k = Scrapers.KaScraper()
    jobs_links = k.extract_job_links()
    candidate_jobs = [k.extract_job(l) for l in jobs_links]
    k.scraper_close()
    for candidate in candidate_jobs:

        if Job.objects.all().filter(ref__contains=candidate.ref):
            pass
        else:
            client = get_client(candidate)
            agent = get_agent(candidate)
            Job.objects.create(
                    ref=candidate.ref,
                    client=client,
                    agent=agent,
                    address=candidate.appointment.address.street,
                    postcode=candidate.appointment.address.postcode,
            )

    return HttpResponse(f'Status: OK. {Job.objects.all().count()} jobs processed.')


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
