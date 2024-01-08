# serializers.py
from rest_framework import serializers
from .models import HospitalImages

class HospitalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalImages
        fields = ['vZipFileName', 'image']
