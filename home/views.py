# home/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import *
from django.core.serializers.json import DjangoJSONEncoder
import json

def dashboard(request):
    hospitals = HospitalMaster.objects.all()
    logos = HospitalLogo.objects.all()
    materials = HospitalPatientAwarenessMaterials.objects.all()
    ThospitalImage = HospitalImages.objects.all()



    total_data_count = hospitals.count() 
    total_logo_count = logos.count() 
    total_materials_count = materials.count() 
    total_hospitalImage_count = ThospitalImage.count() 
    MAX_TOTAL = 100  
    
    
    
    hospitalPercentage = (total_data_count / MAX_TOTAL) * 100  
    logoPercentage = (total_logo_count / MAX_TOTAL) * 100  
    materialsPercentage = (total_materials_count / MAX_TOTAL) * 100  
    hospitalImagePercentage = (total_hospitalImage_count / MAX_TOTAL) * 100  


    for hospital in hospitals:
        print(hospital.vHospitalName)

    context = {
        'hospitals' : hospitals,
        'total_hospitals': hospitals.count(),
        'total_logo' :logos.count(),
        'total_materials' : materials.count(),
        'total_hospitalImage' : ThospitalImage.count(),
        'segment': 'dashboard',
        'hospitalPercentage': hospitalPercentage,
        'logoPercentage': logoPercentage,
        'materialsPercentage': materialsPercentage,
        'hospitalPercentage': hospitalImagePercentage
    }
    return render(request, 'home/admin_index.html', context=context)

def add_hospital(request):
    message = None

    if request.method == 'POST':
        h_name = request.POST.get('hName')
        city = request.POST.get('city')
        state = request.POST.get('states')
        address = request.POST.get('address')
        url = request.POST.get('url')
        status = request.POST.get('status')

        print(f'Hospital Name: {h_name}')
        print(f'City: {city}')
        print(f'State: {state}')
        print(f'Address: {address}')
        print(f'URL: {url}')
        print(f'Status: {status}')

        new_hospital = HospitalMaster(
            vHospitalName=h_name,
            vURL=url,
            vCity=city,
            vState=state,
            vAddress=address,
            eStatus=status
        )

        new_hospital.save()

        message = f"Received the following information from the form:\n\nHospital Name: {h_name}\nCity: {city}"

        return redirect('dashboard_success')

    context = {
        'segment': 'addHospital',
        'message': message,
    }

    return render(request, 'home/add_hospital.html', context=context)


def dashboard_success(request):
    return render(request, 'home/hospitalSuccess.html')


def hospital_list(request):
    hospitals = HospitalMaster.objects.all()

    context = {
        'hospitals': hospitals,
        'segment': 'hospitalList',
        'parent' : 'hospital'
    }
    return render(request, 'home/hospitalList.html', context=context)


def edit_hospital(request, hospital_id):
    hospital = get_object_or_404(HospitalMaster, id=hospital_id)
    return render(request, 'edit_hospital.html', {'hospital': hospital})

def delete_hospital(request, hospital_id):
    hospital = get_object_or_404(HospitalMaster, id=hospital_id)
    hospital.delete()
    return redirect('hospital_list')

def get_hospital_details(request):
    hospital_id = request.GET.get('hospital_id')

    hospital = get_object_or_404(HospitalMaster, id=hospital_id)
    print(hospital.vURL)
    data = {
        'id':hospital.id,
        'vHospitalName': hospital.vHospitalName,
        'vCity': hospital.vCity,
        'vState': hospital.vState,
        'vAddress': hospital.vAddress,
        'vStatus': hospital.eStatus,
        'vURL': hospital.vURL,
    }
    return JsonResponse(data)

@csrf_exempt
def save_edited_hospital(request):
    if request.method == 'POST':
        hospital_id = request.POST.get('EditHospital_ID')
        hospital = get_object_or_404(HospitalMaster, id=hospital_id)

        hospital.vHospitalName = request.POST.get('editHospitalName')
        hospital.vCity = request.POST.get('editCity')
        hospital.vState = request.POST.get('editState')
        hospital.vAddress = request.POST.get('editaddress')

        hospital.eStatus = request.POST.get('editStatus', 'Active')

        hospital.vURL = request.POST.get('editURL')
        print(request.POST.get('editURL'))
        hospital.save()

        return redirect('hospital_list')  

    return JsonResponse({'message': 'Invalid request'}, status=400)

def upload_image(request):
    message = None
    hospitals = HospitalMaster.objects.all()

    if request.method == 'POST':
        h_id = request.POST.get('hName')

        hospital = HospitalMaster.objects.get(id=h_id)

        zip_file = request.FILES.get('zipFile')
        image_file = request.FILES.get('hospitalImage')

        hospital_image = HospitalImages(
            hmid=hospital,
            vZipFileName=zip_file.name if zip_file else None,
            dDateTime=timezone.now(),
            vIP=request.META.get('REMOTE_ADDR'),
            iLoginID=request.user.id if request.user.is_authenticated else None,
            dUDateTime=timezone.now(),
            vUIP=request.META.get('REMOTE_ADDR'),
            image=image_file
        )


        hospital_image.save()
        # return redirect('hospital_list_uploadImage')

    context = {
        'segment': 'addHospital',
        'hospitals': hospitals,
        'message': message,
    }

    return render(request, 'home/add_hospital_images.html', context=context)

def hospital_list_uploadImage(request):
    hospitals = HospitalImages.objects.all()

    context = {
        'hospitals': hospitals,
        'segment': 'hospitalImg',
    }
    return render(request, 'home/hospital_UploadImage_List.html', context=context)


def edit_image(request, image_id):
    image = get_object_or_404(HospitalImages, id=image_id)

    if request.method == "POST":
        gHospital_Name = request.POST.get('editHospitalName')
        gURL = request.POST.get("editURL")
        gCity = request.POST.get("editCity")
        gState = request.POST.get("editState")
        gAddress= request.POST.get("editaddress")
        gStaus = request.POST.get("editStatus")

        image.hmid.vHospitalName = gHospital_Name
        image.hmid.vCity = gURL
        image.hmid.vState = gCity
        image.hmid.vAddress = gState
        image.hmid.vURL = gAddress
        image.hmid.eStatus = gStaus
        image.hmid.save()

        if 'edithospitalImage' in request.FILES:
            hospital_image = request.FILES['edithospitalImage']
            image.image.save(hospital_image.name, hospital_image, save=True)

        if 'editzipFile' in request.FILES:
            zip_file = request.FILES['editzipFile']
            image.vZipFileName.save(zip_file.name, zip_file, save=True)

    
    return redirect("hospital_list_uploadImage")

def delete_image(request, image_id):
    image = get_object_or_404(HospitalImages, id=image_id)
    image.delete()
    return redirect('hospital_list_uploadImage')

def get_image_details(request):
    image_id = request.GET.get('image_id')
    image = get_object_or_404(HospitalImages, hmid=image_id)

    print("hospital ID:", image_id)

    data = {
        'id': image.id,
        'vZipFileName': image.vZipFileName,
        'dDateTime': image.dDateTime.strftime('%Y-%m-%d %H:%M:%S'),
        'vIP': image.vIP,
        'iLoginID': image.iLoginID,
        'dUDateTime': image.dUDateTime.strftime('%Y-%m-%d %H:%M:%S'),
        'vUIP': image.vUIP,
    }


    # Serialize the data using DjangoJSONEncoder
    json_data = json.dumps(data, cls=DjangoJSONEncoder)

    return JsonResponse(json_data, safe=False)

def save_edited_image(request):
    image = get_object_or_404(HospitalImages, id=image_id)

    if request.method == 'POST':
        image_id = request.POST.get('EditHospital_ID')
        print(image_id)

        response_data = {'message': 'Image details saved successfully.'}
        return JsonResponse(response_data)

    return JsonResponse({'message': 'Invalid request'}, status=400)



# Functions to handle Hospital Logo Upload. ( CRUD )
def hospitalLogo_list(request):
    Logos = HospitalLogo.objects.all()

    for logo in Logos:
        if logo.vLogo:
            print(logo.vLogo.url)
        else:
            print("No file associated with vLogo for HospitalLogo ID:", logo.id)

    context = {
        'logos': Logos,
        'segment': 'hospitalLogo',
    }
    return render(request, 'home/hospitalLogo_List.html', context=context)


def upload_Logo(request):
    message = None
    # To get all the hospital Name inside the DropDown . 
    hospitals = HospitalMaster.objects.all()

    if request.method == "POST":
        h_id = request.POST.get('hName')

        hospital = HospitalMaster.objects.get(id=h_id)
        logo_file = request.FILES.get('hospitalLogo')

        hospital_loo = HospitalLogo(
            hmid=hospital,
            vLogo=logo_file,
            dDateTime=timezone.now(),
            vIP=request.META.get('REMOTE_ADDR'),
            dUDateTime=timezone.now(),
            vUIP=request.META.get('REMOTE_ADDR'),
        )

        hospital_loo.save()
        return redirect('hospitalLogo_list')


    context = {
        'segment': 'uploadLogo',
        'hospitals': hospitals,
        'message': message,
    }

    return render(request, 'home/upload_Logo.html', context=context)


def delete_logo(request, image_id):
    logo = get_object_or_404(HospitalLogo, id=image_id)
    logo.delete()
    return redirect('hospitalLogo_list')


def edit_logo(request, image_id):
    logo = get_object_or_404(HospitalLogo, id=image_id)

    if request.method == "POST":
        if 'edithospitalImage' in request.FILES:
            hospital_logo = request.FILES['edithospitalImage']
            logo.vLogo.save(hospital_logo.name, hospital_logo, save=True)
    
    return redirect("hospitalLogo_list")


def patientawareness_List(request):
    pa_list = HospitalPatientAwarenessMaterials.objects.all()

    context = {
        'pa_list': pa_list,
        'segment': 'Patient Awareness',
    }
    
    return render(request, 'home/pa_List.html', context=context)


def upload_paMaterial(request):
    message = None
    # To get all the hospital Name inside the DropDown . 
    hospitals = HospitalMaster.objects.all()

    if request.method == "POST":
        h_id = request.POST.get('hName')

        hospital = HospitalMaster.objects.get(id=h_id)
        file = request.FILES.get('paMaterial')

        hospital_loo = HospitalPatientAwarenessMaterials(
            hmid=hospital,
            vFileName=file,
            dDateTime=timezone.now(),
            vIP=request.META.get('REMOTE_ADDR'),
            dUDateTime=timezone.now(),
            vUIP=request.META.get('REMOTE_ADDR'),
        )

        hospital_loo.save()
        return redirect('patientawareness_List')

    context = {
        'segment': 'uploadpaMaterial',
        'hospitals': hospitals,
        'message': message,
    }

    return render(request, 'home/upload_paMaterial.html', context=context)

def delete_pa(request, image_id):
    pa_material = get_object_or_404(HospitalPatientAwarenessMaterials, id=image_id)
    pa_material.delete()
    return redirect('patientawareness_List')


def edit_paMaterial(request, image_id):
    pa_material = get_object_or_404(HospitalPatientAwarenessMaterials, id=image_id)

    if request.method == "POST":
        if 'edit_paMaterial' in request.FILES:
            hospital_logo = request.FILES['edit_paMaterial']
            print(hospital_logo)
            pa_material.vFileName.save(hospital_logo.name, hospital_logo, save=True)

    return redirect("patientawareness_List")