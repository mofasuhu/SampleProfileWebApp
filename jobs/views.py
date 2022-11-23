from django.shortcuts import render, get_object_or_404
from .models import Job

def home(request):
    jobs = Job.objects
    return render(request, "jobs/home.html", {"jobs": jobs})

def detail(request, pk):
    job = Job.objects.get(pk=pk)
    return render(request, "jobs/detail.html", {"job": job})


