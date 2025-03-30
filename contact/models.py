from django.db import models

# Create your models here.

class Info(models.Model):

    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    place = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Info' # name of the model in admin panel
        verbose_name_plural = 'Infos' 

    def __str__(self):
        return self.email