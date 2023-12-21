# home/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def dashboard(request):
    hospitals = HospitalMaster.objects.all()

    for hospital in hospitals:
        print(hospital.vHospitalName)

    context = {
        'hospitals' : hospitals,
        'total_hospitals': hospitals.count(),
        'segment': 'dashboard'
    }
    return render(request, 'home/admin_index.html', context=context)

def add_hospital(request):
    message = None

    if request.method == 'POST':
        h_name = request.POST.get('hName')
        city = request.POST.get('city')
        state = request.POST.get('states')
        address = request.POST.get('address')
        status = request.POST.get('status')

        print(f'Hospital Name: {h_name}')
        print(f'City: {city}')
        print(f'State: {state}')
        print(f'Address: {address}')
        print(f'Status: {status}')

        new_hospital = HospitalMaster(
            vHospitalName=h_name,
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
        'parent' : 'hospital'
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
    # Add logic for editing hospital
    return render(request, 'edit_hospital.html', {'hospital': hospital})

def delete_hospital(request, hospital_id):
    hospital = get_object_or_404(HospitalMaster, id=hospital_id)
    # Add logic for deleting hospital
    hospital.delete()
    return redirect('hospital_list')

def get_hospital_details(request):
    hospital_id = request.GET.get('hospital_id')
    hospital = get_object_or_404(HospitalMaster, id=hospital_id)
    data = {
        'vHospitalName': hospital.vHospitalName,
        'vCity': hospital.vCity,
        'vState': hospital.vState,
        'vAddress': hospital.vState,
        'vStatus': hospital.vState,
    }
    return JsonResponse(data)

@csrf_exempt
def save_edited_hospital(request):
    if request.method == 'POST':
        hospital_id = request.POST.get('hospital_id')
        hospital = get_object_or_404(HospitalMaster, id=hospital_id)

        hospital.vHospitalName = request.POST.get('editHospitalName')
        hospital.vCity = request.POST.get('editCity')
        hospital.vState = request.POST.get('editState')
        hospital.vAddress = request.POST.get('editaddress')
        hospital.eStatus = request.POST.get('editStatus')
        hospital.save()


        response_data = {'message': 'Hospital details saved successfully.'}
        return JsonResponse(response_data)

    return JsonResponse({'message': 'Invalid request'}, status=400)