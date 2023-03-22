
from django import forms
from .models import Question
from user.models import User

class AskQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        
    