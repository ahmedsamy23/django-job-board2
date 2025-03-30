from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    city = models.ForeignKey('City' , related_name='user_city' , on_delete=models.CASCADE , null=True, blank=True) 
    phone_number = models.CharField(max_length=20 , null=True , blank=True)
    image = models.ImageField(upload_to='profile/' , null=True , blank=True)

    def __str__(self):
        return str(self.user)
    
# create new user ---> create new empty profile
# post_save signal
@receiver(post_save , sender=User)
def create_user_profile(sender , instance , created , **kwargs):
    if created:
        Profile.objects.create(user=instance)
# post_save signal: يتم ارسالها بعد حفظ البيانات في قاعدة البيانات
# sender: هو المرسل للسيجنال
# instance: هو الكائن الذي تم حفظه
# created: هل تم انشاء الكائن ام لا
# **kwargs: هو البيانات الاضافية التي يمكن ان تكون مرفقة مع السيجنال
# sender=User: هو الكلاس الذي يتم ارسال السيجنال منه


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name