from django.db import models
from user.models import User
from django.conf import settings
# from models import *

# Create your models here.

class TechnologyLabel(models.Model):
    label = models.CharField(max_length=25)

    class Meta:
        db_table = 'technology_label'


        
class Question(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    status = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table = 'question'

    def __str__(self):
        return self.title


class Answers(models.Model):
    answer = models.CharField(max_length=1000)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    likeCount = models.IntegerField()
    dislikeCount = models.IntegerField()
    markAsSolution = models.IntegerField()
    docUrl = models.CharField(max_length=250)

    class Meta:
        db_table = 'answers'

    

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
    rank = models.IntegerField()

    class Meta:
        db_table = 'badges'


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



