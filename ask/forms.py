
from django import forms
from .models import *
from user.models import User
from django.db import transaction

class AskQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

    # @transaction.atomic
    # def save(self):
    #     user = super().save(commit=0)
    #     user.status = 1
    #     user.save()
    #     return user
        

class QuestionAnswerForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = ('answer','user','question','docUrl') 

 