from django import views
from django.contrib import admin
from django.urls import path,include
from .views import *
from . import views

urlpatterns = [
    path('ask_question/',AskQuestionView.as_view(),name='ask_question'),
    path('list_question/',QuestionListView.as_view(),name='question_list'),
    path('delete_question/<int:pk>',QuestionDeleteView.as_view(),name='delete_question'),
    path('update_question/<int:pk>',QuestionUpdateView.as_view(),name='update_question'),
    path('detail_question/<int:pk>',QuestionDetailView.as_view(),name='detail_question'),
    path('answer_question/<int:pk>',QuestionAnswerView.as_view(),name='answer_question'),
    path('update_answer/<int:pk>',AnswerUpdateView.as_view(),name='update_answer'),
    path('delete_answer/<int:pk>',AnswerDeleteView.as_view(),name='delete_answer'),
    path('technologylist/',TechnologyListView.as_view(),name='technology_list'),
    path('badgeslist/',BadgesListView.as_view(),name='badges_list'),
    path('likes/',views.like),
    path('dislikes/',views.dislike)
]