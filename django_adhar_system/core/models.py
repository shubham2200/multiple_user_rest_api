from os import name
from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class User(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# class Address(models.Model):
#     user = models.OneToOneField(User ,on_delete=models.CASCADE, related_name='manager')
#     street = models.CharField(max_length=100 , blank=True , null=True)
#     city = models.CharField(max_length=25 , blank=True , null=True)
#     state = models.CharField(max_length=20 , blank=True , null=True)
#     postal_code = models.CharField(max_length=7 , blank=True , null=True)
#     def __str__(self):
#         return self.user.username

# class Adhar(models.Model):
#     user = models.OneToOneField(User ,on_delete=models.CASCADE, related_name='staff')
#     number = models.CharField(max_length=100 , blank=True , null=True)
#     name = models.CharField(max_length=100 , blank=True , null=True)
#     def __str__(self):
#         return self.user.username

class Aadhar(models.Model):
    aadhar_number = models.CharField(max_length=12  ,unique=True, primary_key=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.aadhar_number

class Address(models.Model):
    aadhar = models.ForeignKey(Aadhar , on_delete=models.CASCADE , related_name='address')
    street = models.CharField(max_length=10, blank=True,null=True)
    city = models.CharField(max_length=10, blank=True,null=True)
    state = models.CharField(max_length=10, blank=True,null=True)
    postal_code = models.CharField(max_length=7, blank=True,null=True)
    

class Qalification(models.Model):
    aadhar = models.ForeignKey(Aadhar , on_delete=models.CASCADE , related_name='qalification')
    name_collage_school = models.CharField(max_length=15 , null=True , blank=True)
    Year_passing = models.DateField(

    )
    percentage = models.FloatField()
    def __str__(self):
        return self.name_collage_school


class Bank(models.Model):
    aadhar = models.ForeignKey(Aadhar , on_delete=models.CASCADE , related_name='bank')   
    account_number = models.CharField(max_length=16 , blank=True,null=True )
    bank_name = models.CharField(max_length=16 , blank=True,null=True )
    ifcs = models.CharField(max_length=6 , unique=True,blank=True,null=True )
    def __str__(self):
        return self.account_number
    

class PersonalDetails(models.Model):
    aadhar = models.ForeignKey(Aadhar , on_delete=models.CASCADE , related_name='PersonalDetails')  
    CHOICES = (
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('A+' , 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ) 
    fullname = models.CharField(max_length=30 , blank=True,null=True )
    date_of_brith = models.DateField()
    bloodgroup = models.CharField(max_length=3 , choices=CHOICES)
    contact_number =  PhoneNumberField(unique=True ,blank=True, null=True )
    email = models.EmailField()
    def __str__(self):
        return self.fullname

class PastJobExperience(models.Model):
    aadhar = models.ForeignKey(Aadhar , on_delete=models.CASCADE , related_name='PastJobExperience')
    company_name = models.CharField(max_length=19 , blank=True , null=True)
    job_role =  models.CharField(max_length=19 , blank=True , null=True)
    year_of_work_experience = models.CharField(max_length=19 , blank=True , null=True)
    def __str__(self):
        return self.company_name


