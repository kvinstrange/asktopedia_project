from telnetlib import LOGOUT
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import *
from .forms import *
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login,logout
from django import forms
from django.views import View
from django.views.generic import ListView,TemplateView,DetailView,UpdateView
from ask.models import Question
from django.contrib.auth import get_user_model

# Create your views here.

class UserRegisterview(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/user_register.html'
    success_url = '/user/login'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'user'
        return super().get_context_data(**kwargs)

    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)



class UserLoginView(LoginView):
    template_name = 'user/login.html'

    def get_redirect_url(self):
        if self.request.user.is_authenticated:   
            return '/user/user/dashboard'
            

            

class UserLogoutView(TemplateView):
    template_name = 'user/logout.html'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse_lazy('dashboard'))
    


class DashBoardView(ListView):
    # model = User
    template_name = 'user/dashboard.html'
    
    def get(self, request, *args, **kwargs):
        question = Question.objects.all().values()
        return render(request, 'user/dashboard.html',{
            'questions':question,
        })
    
    def get_queryset(self):
        return super().get_queryset()



class UserDashBoardView(ListView):
    # model = User
    template_name = 'user/user_dashboard.html'
    
    def get(self, request, *args, **kwargs):
        question = Question.objects.all().values()
        return render(request, 'user/user_dashboard.html',{
            'questions':question,
        })
    
    def get_queryset(self):
        return super().get_queryset()
    
  

class UserProfileView(DetailView):
    model = User
    template_name = 'user/user_profile.html'
    context_object_name = 'user_profile'



class UserUpdateView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'user/user_update.html'
    success_url = 'user/userprofile/'



class ContactUsView(CreateView):
    form_class = ContactUsForm
    model = ContactUs
    template_name = 'home.html'
    success_url = ''
    
    def form_valid(self, form):
        return super().form_valid(form)
