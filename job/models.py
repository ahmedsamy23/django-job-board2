from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
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
    return 'jobs/%s.%s'%(instance.id , extension)

class Job(models.Model):

    JOB_TYPE = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        )
    owner = models.ForeignKey(User , on_delete=models.CASCADE , related_name='job_owner')
    title = models.CharField(max_length=50)
    #location = 
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now_add=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE , null=True)
    image = models.ImageField(upload_to=image_upload)
    
    slug = models.SlugField(blank= True , null=True) # slug = title

    # def save(self , *args , **kwargs):
    #     self.slug = slugify(self.title) # slugify :  تحويل النص الى نص مفهرس
    #     super(Job , self).save(*args , **kwargs)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        if self.image and hasattr(self.image, 'file'):
            try:
                resized_image = resize_image(self.image, size=(100, 100))
                self.image.save(
                    f"{self.slug}.{self.image.name.split('.')[-1]}",
                    resized_image,
                    save=False
                )
            except Exception as e:
                print(f"Error resizing image: {e}")

        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Apply(models.Model):

    job = models.ForeignKey(Job , on_delete=models.CASCADE , related_name='apply_job')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name