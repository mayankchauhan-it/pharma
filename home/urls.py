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
    # upload image urls

    path('dashboard/hospitals_upload_image/', hospital_list_uploadImage, name='hospital_list_uploadImage'),
    path('upload_image/', upload_image, name='upload_image'),
    path('edit_image/<int:image_id>/', edit_image, name='edit_image'),
    path('delete_image/<int:image_id>/', delete_image, name='delete_image'),
    path('get_image_details/', get_image_details, name='get_image_details'),
    path('save_edited_image/', save_edited_image, name='save_edited_image'),


    path('dashboard/upload_hospitalLogo/', hospitalLogo_list, name='hospitalLogo_list'),
    path('upload_Logo/', upload_Logo, name='upload_Logo'),
    path('edit_logo/<int:image_id>/', edit_logo, name='edit_logo'),
    path('delete_logo/<int:image_id>/', delete_logo, name='delete_logo'),

    # Patient Awareness 
    path('dashboard/patientawareness_List/', patientawareness_List, name='patientawareness_List'),
    path('upload_paMaterial/', upload_paMaterial, name='upload_paMaterial'),
    path('edit_paMaterial/<int:image_id>/', edit_paMaterial, name='edit_paMaterial'),
    path('delete_pa_material/<int:image_id>/', delete_pa, name='delete_pa'),

]