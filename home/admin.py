from django.contrib import admin
from .models import *

# Register the HospitalMaster model with the admin site
admin.site.register(HospitalMaster)
admin.site.register(HospitalImages)