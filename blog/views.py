from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Blog , CommentBlog
from .forms import BlogForm , CommentForm
from .filters import BlogFilter
from django.contrib import messages
# Create your views here.


def blog_list(request):
    
    blogs = Blog.objects.all()
     
    # Filters:
    myfilter = BlogFilter(request.GET , queryset=blogs)
    blogs = myfilter.qs


    paginator = Paginator(blogs , 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request , 'blog/blog_list.html' , {'blogs':page_obj , 'myfilter':myfilter})

def blog_detail(request , slug):

    blog_detail = Blog.objects.get(slug=slug)
    comments = CommentBlog.objects.filter(blog=blog_detail)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.blog = blog_detail
            
            if request.user.is_authenticated:
                myform.user = request.user
                myform.save()
                return redirect(reverse('blog:blog_detail' , kwargs={'slug':blog_detail.slug})) 
            else:
                return redirect(reverse('accounts:signup'))
    else:
        form = CommentForm()
    return render(request , 'blog/blog_detail.html' , {'blog':blog_detail , 'form':form , 'comments':comments})


@login_required
def edit_blog(request , slug):

    blog_detail = Blog.objects.get(slug=slug)
    if request.user != blog_detail.author:
        messages.error(request , 'You are not authorized to edit this blog.')
        return redirect(reverse('blog:blog_detail' , kwargs={'slug':blog_detail.slug}))
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES  ,instance=blog_detail)
        if form.is_valid():
            form.save()
            messages.success(request , 'Blog Updated Successfully')
            return redirect(reverse('blog:blog_detail' , kwargs={'slug':blog_detail.slug}))
    else:
        form = BlogForm(instance=blog_detail)
    return render(request , 'blog/edit_blog.html' , {'blog':blog_detail , 'form':form})


@login_required
def add_blog(request):
    
    if request.method == 'POST':
        form = BlogForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect(reverse('blog:blog_list'))
    else:
        form = BlogForm()
    return render(request , 'blog/add_blog.html' , {'form':form})
