from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
# Create your models here.


def resize_image(image_field, size=(100, 100)):
    img = Image.open(image_field)
    img = img.resize(size, Image.LANCZOS)
    thumb_io = BytesIO()
    img.save(thumb_io, format=img.format if img.format else 'PNG')
    thumb_file = ContentFile(thumb_io.getvalue())
    return thumb_file

def image_upload(instance , filename):
    imagename , extension = filename.split('.')
    return 'blogs/%s.%s'%(instance.id , extension)

class Blog(models.Model):
    
    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name='blog_author')
    title = models.CharField(max_length=100)
    body = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=image_upload , blank=True , null=True)

    slug = models.SlugField(blank= True , null=True) # slug = title

    def save(self , *args , **kwargs):
        self.slug = slugify(self.title) # slugify :  تحويل النص الى نص مفهرس
        super(Blog , self).save(*args , **kwargs)

    def __str__(self):
        return self.title
    

class CommentBlog(models.Model):
    blog = models.ForeignKey(Blog , on_delete=models.CASCADE , related_name='blog_comment')
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='blog_user')
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} comment on {self.blog.title}"