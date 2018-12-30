from django.http import HttpResponse
from django.shortcuts import render
from EstateAgent import Scrapers


# Create your views here.
def index(request):
    k = Scrapers.KaScraper()
    jobs_links = k.extract_job_links()
    hips = '\n'.join([k.extract_job(l).id for l in jobs_links])
    k.scraper_close()
    return HttpResponse(hips)
