from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField

class User(AbstractUser):
    pass

class Patient(models.Model):
    GENDER=(
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
    )
    
    full_name = models.CharField(max_length=25)
    age = models.IntegerField(default=0)
    phone = models.CharField(max_length=15)
    gender=models.CharField(max_length=8,choices=GENDER,default='Others')
    address=models.TextField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.full_name}"

class Doctor (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.user.username
    
class Records(models.Model):
    EQUIPMENTS=(
        ('IFT','IFT'),
        ('WAX','WAX'),
        ('ULTRA SOUND','ULTRA SOUND'),
        ('MICROWAVE','MICROWAVE'),
        ('STIMULATION','STIMULATION'),
        ('TENS','TENS'),
        ('TRACTION','TRACTION'),
        ('CPM','CPM'),
    )
    
    
    OTHER_REPORTS=(
        ('MRI',"MRI"),
        ('X-ray',"X-ray"),
        ('CT scan',"CT scan"),    
    )
    
    patient=models.ForeignKey('Patient',on_delete=models.CASCADE,related_name='records')
    patient_cause=models.CharField(max_length=100)
    reports=MultiSelectField(max_length=30,choices=OTHER_REPORTS,null=True,blank=True)
    treatments=MultiSelectField(max_length=40,choices=EQUIPMENTS,null=True,blank=True)
    doctor = models.ForeignKey("Doctor",on_delete=models.CASCADE,null=True,blank=True)
    created_on=models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self) -> str:
        return self.patient.full_name