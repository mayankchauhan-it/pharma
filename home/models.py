# hospital/models.py

from django.db import models
from django.utils import timezone


def get_upload_path(instance, filename):
    return f'{instance.hmid.id}/hospital_images/{filename}'


def get_Logo_upload_path(instance, filename):
    return f'{instance.hmid.id}/Hospital Logo/{filename}'

def get_paMaterial_upload_path(instance, filename):
    return f'{instance.hmid.id}/Hospital Patient Awareness Material/{filename}'

class HospitalMaster(models.Model):
    id = models.AutoField(primary_key=True)
    vHospitalName = models.CharField(max_length=255)
    vCity = models.CharField(max_length=255)
    vState = models.CharField(max_length=255)
    vAddress = models.CharField(max_length=255)
    vURL = models.CharField(max_length = 255, blank=True, null=True)
    eStatus = models.CharField(max_length=10,  blank=True, null=True)

    def __str__(self):
        return str(self.id) + " " + self.vHospitalName + " ("+self.eStatus+")"

class HospitalImages(models.Model):
    id = models.AutoField(primary_key=True)
    hmid = models.ForeignKey(HospitalMaster, on_delete=models.CASCADE)
    vZipFileName = models.FileField(upload_to=get_upload_path, blank=True, null=True)
    dDateTime = models.DateTimeField(default=timezone.now)
    vIP = models.CharField(max_length=255)
    iLoginID = models.IntegerField(blank=True, null=True)
    dUDateTime = models.DateTimeField(default=timezone.now)
    vUIP = models.CharField(max_length=255)
    image = models.ImageField(upload_to=get_upload_path, blank=True, null=True)

    def __str__(self):
        return self.hmid.vHospitalName

class HospitalLogo(models.Model):
    id = models.AutoField(primary_key=True)
    hmid = models.ForeignKey(HospitalMaster, on_delete=models.CASCADE)
    vLogo = models.ImageField(upload_to=get_Logo_upload_path, blank=True, null=True)
    dDateTime = models.DateTimeField()
    vIP = models.CharField(max_length=255)
    dUDateTime = models.DateTimeField()
    vUIP = models.CharField(max_length=255)

    def __str__(self):
        return self.hmid.vHospitalName

class HospitalPatientAwarenessMaterials(models.Model):
    id = models.AutoField(primary_key=True)
    hmid = models.ForeignKey(HospitalMaster, on_delete=models.CASCADE)
    vFileName = models.FileField(upload_to=get_paMaterial_upload_path, blank=True, null=True)
    dDateTime = models.DateTimeField()
    vIP = models.CharField(max_length=255)
    dUDateTime = models.DateTimeField()
    vUIP = models.CharField(max_length=255)

    def __str__(self):
        return self.hmid.vHospitalName

class HospitalTiming(models.Model):
    id = models.AutoField(primary_key=True)
    hmid = models.ForeignKey(HospitalMaster, on_delete=models.CASCADE)
    vFileName = models.CharField(max_length=255)
    dDateTime = models.DateTimeField()
    vIP = models.CharField(max_length=255)
    dUDateTime = models.DateTimeField()
    vUIP = models.CharField(max_length=255)

    def __str__(self):
        return self.hmid.vHospitalName

class HospitalDoctorProfile(models.Model):
    id = models.AutoField(primary_key=True)
    hmid = models.ForeignKey(HospitalMaster, on_delete=models.CASCADE)
    vFileName = models.CharField(max_length=255)
    dDateTime = models.DateTimeField()
    vIP = models.CharField(max_length=255)
    dUDateTime = models.DateTimeField()
    vUIP = models.CharField(max_length=255)

class HospitalFacilities(models.Model):
    id = models.AutoField(primary_key=True)
    hmid = models.ForeignKey(HospitalMaster, on_delete=models.CASCADE)
    vFileName = models.CharField(max_length=255)
    dDateTime = models.DateTimeField()
    vIP = models.CharField(max_length=255)
    dUDateTime = models.DateTimeField()
    vUIP = models.CharField(max_length=255)

class HospitalAchievements(models.Model):
    id = models.AutoField(primary_key=True)
    hmid = models.ForeignKey(HospitalMaster, on_delete=models.CASCADE)
    vFileName = models.CharField(max_length=255)
    dDateTime = models.DateTimeField()
    vIP = models.CharField(max_length=255)
    dUDateTime = models.DateTimeField()
    vUIP = models.CharField(max_length=255)

class HospitalSocialMediaLinks(models.Model):
    id = models.AutoField(primary_key=True)
    hmid = models.ForeignKey(HospitalMaster, on_delete=models.CASCADE)
    vLinkedIn = models.CharField(max_length=255)
    vTwitter = models.CharField(max_length=255)
    vInstagram = models.CharField(max_length=255)
    vFaceBook = models.CharField(max_length=255)
    vYoutube = models.CharField(max_length=255)
    vSocial1 = models.CharField(max_length=255)
    vSocial2 = models.CharField(max_length=255)
    dDateTime = models.DateTimeField()
    vIP = models.CharField(max_length=255)
    dUDateTime = models.DateTimeField()
    vUIP = models.CharField(max_length=255)
