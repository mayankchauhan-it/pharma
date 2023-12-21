# home/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/addhospital', add_hospital, name='add_hospital'),
    path('dashboard/success/', dashboard_success, name='dashboard_success'),
    path('dashboard/hospitals/', hospital_list, name='hospital_list'),
    path('dashboard/edit_hospital/<int:hospital_id>/', edit_hospital, name='edit_hospital'),
    path('dashboard/delete_hospital/<int:hospital_id>/', delete_hospital, name='delete_hospital'),
    path('get_hospital_details/', get_hospital_details, name='get_hospital_details'),
    path('save_edited_hospital/', save_edited_hospital, name='save_edited_hospital'),
    # Add other paths as needed
]
