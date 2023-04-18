from django.db import models
from django.contrib.auth.models import AbstractUser
# from ask.models import TechnologyLabel

# Create your models here.


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    gender = models.CharField(max_length=25)
    qualification = models.CharField(max_length=50)

    class Meta:
        db_table = 'users'

    

class User_Technology(models.Model):
    technologylabel = models.ForeignKey("ask.TechnologyLabel",on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_technology'


class ContactUs(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=30)
    message = models.CharField(max_length=200)

    class Meta:
        db_table = 'contactUs'