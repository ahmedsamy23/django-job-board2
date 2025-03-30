from django.shortcuts import render
from job.models import Job
from job.models import Category

# Create your views here.


def home(request):

    jobs_list = Job.objects.all().order_by('-published_at')[:5]
    categories = Category.objects.all()
    
    return render(request , 'home.html' , {'jobs_list':jobs_list , 'categories':categories})