from django.shortcuts import render , redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.paginator import Paginator 
from .forms import ApplyForm , JobForm
from .filters import JobFilter
# pagination :  عندما تكون البيانات كبيرة جدا ولا يمكن عرضها في صفحة واحدة يمكنك تقسيمها على عدة صفحات

# Create your views here.

def job_list(request):
    
    job_list = Job.objects.all()

    # Filters:
    myfilter = JobFilter(request.GET , queryset=job_list) # queryset : هي النتيجة التي سيتم تصفيتها
    job_list = myfilter.qs # qs : هي النتيجة التي تم تصفيتها

    paginator = Paginator(job_list , 5) # 2 is the number of jobs per page
    page_number = request.GET.get('page') # get the page number from the url
    page_obj = paginator.get_page(page_number)  # get the page object from the paginator



    return render(request , 'job/job_list.html' , {'jobs':page_obj , 'myfilter':myfilter})

def job_detail(request , slug):
    
    job_detail= Job.objects.get(slug=slug)
    if request.method =='POST':
        form = ApplyForm(request.POST , request.FILES) # request.FILES to upload files
        if form.is_valid():
            myform = form.save(commit=False) # commit=False to save the form without saving it to the database
            myform.job = job_detail # job_detail is the job that the user applied for
            myform.save()
    else :
        form = ApplyForm()

    return render(request , 'job/job_detail.html' , {'job':job_detail , 'form1':form})

@login_required
def add_job(request):

    if request.method == 'POST':
        form = JobForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user # request.user is the user that is logged in
            myform.save()
            return redirect(reverse('jobs:job_list')) # reverse :  يقوم بتحويل الاسم الى الرابط المرتبط به
            # jobs is the namespace and job_list is the name of the base url
            # job_list is the name of the url
    else:
        form = JobForm()
    return render(request , 'job/add_job.html' , {'form':form})