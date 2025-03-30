
from django.urls import path
from . import api
from . import views


app_name = 'blog'
urlpatterns = [
    path('' , views.blog_list , name='blog_list'),
    path('add_blog/' , views.add_blog , name='add_blog'),
    path('<str:slug>' , views.blog_detail , name='blog_detail'),
    path('edit_blog/<str:slug>' , views.edit_blog , name='edit_blog'),

    # api:
    path('api/blogs' , api.BlogListApi.as_view() , name='blog_list_api'),
    path('api/blogs/<int:id>' , api.BlogDetailApi.as_view() , name='blog_detail_api'),
]