from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.models import User
from .models import Profile
from job.models import Job
from blog.models import Blog
from .forms import SignupForm , UserForm , ProfileForm 
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.

# explain the signup view
# 1- if the request method is post
# 2- if the form is valid
# 3- create user and login
# 4- redirect to profile page
# authenticate: يقوم بالتحقق من البيانات المدخلة في النموذج والتاكد من صحة البيانات والتاكد من ان البيانات صحيحة
# login: اذا كانت البيانات صحيحة يقوم بتسجيل الدخول للمستخدم
def signup(request):
    
    if request.method == 'POST':
        form  = SignupForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username , password=password)
            login(request , user)  
            return redirect('/accounts/profile')           
    else:
        form = SignupForm()
    return render(request , 'registration/signup.html' , {'form':form})




def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request , 'accounts/profile.html' , {'profile':profile})

def profile_edit(request):
    profile = Profile.objects.get(user = request.user)

    if request.method== 'POST':
        userform = UserForm(request.POST , instance=request.user)
        profileform = ProfileForm(request.POST , request.FILES  ,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect('accounts:profile')
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    return render(request , 'accounts/profile_edit.html' , {'userform':userform , 'profileform':profileform})



# def favourites(request):
#     love_job = Job.objects.filter(love=request.user)
#     love_blog = Blog.objects.filter(love=request.user)
#     return render(request , 'accounts/favourites.html' , {'love_job':love_job , 'love_blog':love_blog})

# @csrf_exempt
# @login_required
# def love_item(request , item_type , item_id):
#     if request.method == 'POST':
#         user = request.user
#         if item_type == 'job':
#             item = get_object_or_404(Job , id=item_id)
#         elif item_type == 'blog':
#             item = get_object_or_404(Blog , id=item_id)
#         else:
#             return JsonResponse({'error':'Invalid item type'} , status=400)
        
#         if user in item.love.all():
#             item.love.remove(request.user)
#             loved = False
#         else:
#             item.love.add(request.user)
#             loved = True
#         return JsonResponse({'loved':loved})

#     return JsonResponse({'error':'Invalid request method'} , status=400)
    