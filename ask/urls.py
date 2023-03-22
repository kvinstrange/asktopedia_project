from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('create_question/',AskQuestionView.as_view(),name='create_question'),
    path('list_question/',QuestionListView.as_view(),name='question_list'),
    path('delete_question/<int:pk>',QuestionDeleteView.as_view(),name='delete_question'),
    path('update_question/<int:pk>',QuestionUpdateView.as_view(),name='update_question'),
]