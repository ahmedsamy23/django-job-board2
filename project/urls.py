"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('' , include('home.urls' , namespace='home')),
    path('accounts/' , include('django.contrib.auth.urls')), # include all urls of django.contrib.auth
    path('accounts/' , include('accounts.urls' , namespace='accounts')), # include all urls of accounts app
    path('admin/', admin.site.urls),
    path('jobs/' , include('job.urls' , namespace='jobs')),
    path('blog/' , include('blog.urls' , namespace='blog')),
    path('contact-us/' , include('contact.urls' , namespace='contact')),
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# namespace:  هو اسم يتم تحديده للتعرف على التطبيق الذي يتم توجيه اليه الطلب
# in html : <a href="{% url 'jobs:job_list' %}">Jobs</a> # jobs is the namespace and job_list is the name of the url