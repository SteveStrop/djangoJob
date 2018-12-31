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
from jobs.models import Job


class IndexListView(generic.ListView):
    model = Job


class JobDetailView(generic.DetailView):
    model = Job
