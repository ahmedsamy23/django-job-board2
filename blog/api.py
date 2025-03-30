from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer

class BlogListApi(generics.ListCreateAPIView):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'id' # to get the blog by id