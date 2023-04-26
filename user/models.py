from django.db import models
from django.contrib.auth.models import AbstractUser
# from ask.models import TechnologyLabel

# Create your models here.


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    gender = models.CharField(max_length=25,null=True)
    qualification = models.CharField(max_length=50,null=True)
    bio = models.CharField(max_length=100,null=True)
    age = models.IntegerField(null=True)
    phone = models.IntegerField(null=True)
    profilepic = models.ImageField(upload_to='image/',null=True,blank=True,default='media/avatar7.png')

    class Meta:
        db_table = 'users'

    

class User_Technology(models.Model):
    technologylabel = models.ForeignKey("ask.TechnologyLabel",on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_technology'

