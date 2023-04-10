from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import AdminRegisterForm,UserRegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django import forms
from django.views import View
from django.views.generic import ListView
from ask.models import Question

# Create your views here.

class AdminRegisterView(CreateView):
    model = User
    form_class = AdminRegisterForm
    template_name = 'user/admin_register.html'
    success_url = '/user/login'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        #email = form.cleaned_data.get('email')
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)



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
    # form_class = LoginForm

    def get_redirect_url(self):
        if self.request.user.is_authenticated:    
            if self.request.user.is_admin:
                return '/user/admin/dashboard'
            else:
                return '/user/user/dashboard'
            


class AdminDashboardView(ListView):            
    template_name = 'user/admin_dashboard.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
        
    def get_queryset(self):
        return super().get_queryset()




class UserDashBoardView(ListView):
    # model = User
    template_name = 'user/user_dashboard.html'
    
    def get(self, request, *args, **kwargs):
        question = Question.objects.all().values()
        return render(request, 'user/admin_dashboard.html',{
            'questions':question,
        })
    
    def get_queryset(self):
        return super().get_queryset()
    
   
    