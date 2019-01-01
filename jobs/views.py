from django.http import HttpResponse
from django.shortcuts import render
from EstateAgent import Scrapers
from django.views import generic

# Create your views here.
# def index(request):
#     k = Scrapers.KaScraper()
#     jobs_links = k.extract_job_links()
#     hips = '\n'.join([k.extract_job(l).id for l in jobs_links])
#     k.scraper_close()
#     return HttpResponse(hips)
from jobs.models import Job, Vendor


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
