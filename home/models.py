# hospital/models.py

from django.db import models

class HospitalMaster(models.Model):
    id = models.AutoField(primary_key=True)
    vHospitalName = models.CharField(max_length=255)
    vCity = models.CharField(max_length=255)
    vState = models.CharField(max_length=255)
    vAddress = models.CharField(max_length=255)
    eStatus = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])

    def __str__(self):
        return str(self.id) + " " + self.vHospitalName + " ("+self.eStatus+")"

class HospitalImages(models.Model):
    id = models.AutoField(primary_key=True)
    hmid = models.ForeignKey(HospitalMaster, on_delete=models.CASCADE)
    vZipFileName = models.CharField(max_length=255)
    dDateTime = models.DateTimeField()
    vIP = models.CharField(max_length=255)
    iLoginID = models.IntegerField()
    dUDateTime = models.DateTimeField()
    vUIP = models.CharField(max_length=255)

    def __str__(self):
        return self.hmid.vHospitalName

class HospitalLogo(models.Model):
    id = models.AutoField(primary_key=True)
    hmid = models.ForeignKey(HospitalMaster, on_delete=models.CASCADE)
    vLogoID = models.CharField(max_length=255)
    dDateTime = models.DateTimeField()
    vIP = models.CharField(max_length=255)
    iLoginID = models.IntegerField()
    dUDateTime = models.DateTimeField()
    vUIP = models.CharField(max_length=255)

    def __str__(self):
        return self.hmid.vHospitalName

class HospitalPatientAwarenessMaterials(models.Model):
    id = models.AutoField(primary_key=True)
    hmid = models.ForeignKey(HospitalMaster, on_delete=models.CASCADE)
    vFileName = models.CharField(max_length=255)
    dDateTime = models.DateTimeField()
    vIP = models.CharField(max_length=255)
    iLoginID = models.IntegerField()
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
    iLoginID = models.IntegerField()
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
    iLoginID = models.IntegerField()
    dUDateTime = models.DateTimeField()
    vUIP = models.CharField(max_length=255)

class HospitalFacilities(models.Model):
    id = models.AutoField(primary_key=True)
    hmid = models.ForeignKey(HospitalMaster, on_delete=models.CASCADE)
    vFileName = models.CharField(max_length=255)
    dDateTime = models.DateTimeField()
    vIP = models.CharField(max_length=255)
    iLoginID = models.IntegerField()
    dUDateTime = models.DateTimeField()
    vUIP = models.CharField(max_length=255)

class HospitalAchievements(models.Model):
    id = models.AutoField(primary_key=True)
    hmid = models.ForeignKey(HospitalMaster, on_delete=models.CASCADE)
    vFileName = models.CharField(max_length=255)
    dDateTime = models.DateTimeField()
    vIP = models.CharField(max_length=255)
    iLoginID = models.IntegerField()
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
    iLoginID = models.IntegerField()
    dUDateTime = models.DateTimeField()
    vUIP = models.CharField(max_length=255)

# UserMaster model can be defined based on your requirements
