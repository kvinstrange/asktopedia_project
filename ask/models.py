from django.db import models
from user.models import User
from django.conf import settings
# from models import *

# Create your models here.

class TechnologyLabel(models.Model):
    labeltitle = models.CharField(max_length=25,null=True)
    label = models.CharField(max_length=100)

    class Meta:
        db_table = 'technology_label'

    def __str__(self):
        return self.labeltitle


        
class Question(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    status = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    tag = models.CharField(max_length=100,null=True)
    class Meta:
        db_table = 'question'

    def __str__(self):
        return self.title


class Answers(models.Model):
    answer = models.CharField(max_length=1000)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True) 
    question = models.ForeignKey(Question,on_delete=models.CASCADE,null=True)
    likeCount = models.IntegerField(default=0,null=True)
    dislikeCount = models.IntegerField(default=0,null=True)
    markAsSolution = models.IntegerField(default=0,null=True)
    docUrl = models.FileField(upload_to='upload/',null=True,blank=True)

    class Meta:
        db_table = 'answers'

    
    def __str__(self):
        return self.answer
    

# class Meetup(models.Model):
#     author = models.ForeignKey(User,on_delete=models.CASCADE)
#     speaker = models.ForeignKey(User,on_delete=models.CASCADE)
#     url = models.CharField(max_length=100)
#     meetUpProposal = models.CharField(max_length=1000)
#     datetime = models.CharField(max_length=50)
#     duration = models.IntegerField()
#     isAccepted = models.IntegerField()

#     class Meta:
#         db_table = 'meetup'


# class Meetup_Participants(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     meetup = models.ForeignKey(Meetup,on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'meetup_participants'


class Badges(models.Model):
    badgetitle = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    rank = models.IntegerField(default=0)

    class Meta:
        db_table = 'badges'

    def __str__(self):
        return self.badgetitle


class User_Badges(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    badge = models.ForeignKey(Badges,on_delete=models.CASCADE)
    earnDate = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'user_badges'


class Tutorials(models.Model):
    technologylabel = models.ForeignKey(TechnologyLabel,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    url = models.CharField(max_length=250)
    isApproved = models.IntegerField()
    rejectReason = models.CharField(max_length=200)

    class Meta:
        db_table = 'tutorials'



