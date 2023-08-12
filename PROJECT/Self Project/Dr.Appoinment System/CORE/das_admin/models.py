from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser 

# Create your models here.

# class User(AbstractUser):
#     usertype = models.CharField(max_length=20)



#    Doctor  Profile  table model

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    reg_no = models.CharField(max_length=20)
    gender = models.CharField(max_length=15, null=True, blank=True)
    picture = models.ImageField(upload_to='doctor_pictures')
    status = models.BooleanField(default=True, blank=True, null=True)
    fees = models.IntegerField(default=0, blank=True, null=True)
    salary = models.IntegerField(default=0, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    speciality= models.CharField(max_length=100)
    service = models.CharField(max_length= 100)
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    starting_year = models.PositiveIntegerField()
    completion_year = models.PositiveIntegerField()
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    seat_no = models.CharField(max_length=20, null=True, blank=True)

#    Doctor  Address  table model

class DoctorAddress(models.Model):
    doctor = models.OneToOneField(User, on_delete=models.CASCADE)
    add_line_1 = models.CharField(max_length=100, null=True, blank=True)
    add_line_2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)


#    Doctor Time Schedule Details table model

class DoctorTimeSchedule(models.Model):
    doctor = models.ForeignKey('DoctorProfile', on_delete=models.CASCADE)
    day = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()    

#    Doctor Appointment Details table model

# class DoctorAppointmentDetails(models.Model):
#     doctor = models.ForeignKey('DoctorProfile', on_delete=models.CASCADE)
#     patient = models.ForeignKey('PatientProfile', on_delete=models.CASCADE)
#     appointment_date = models.DateField()
#     appointment_time = models.TimeField()
#     notes = models.TextField(blank=True)    


