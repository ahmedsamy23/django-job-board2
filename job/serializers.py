## serializers : get data from database and convert it into json format
from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Job
        fields = '__all__' # to get all fields from the model