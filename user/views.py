from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import *
from .forms import *
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView
from django.contrib.auth import login,logout
from django import forms
from django.views import View
from django.views.generic import ListView,TemplateView,DetailView,UpdateView
from ask.models import Question
from django.contrib.auth import get_user_model
from ask.models import User_Badges, Badges,Answers,Question
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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
        return redirect(reverse_lazy('home'))
    


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


@method_decorator(login_required(login_url='/user/login'), name='dispatch')
class UserDashBoardView(ListView):
    # model = User
    template_name = 'user/user_dashboard.html'
    model = Question
    context_object_name = 'title'
    
    def get(self, request, *args, **kwargs):
        question = Question.objects.all().values()
        sort_by = self.request.GET.get('sort_by', 'title')
        direction = self.request.GET.get('direction', 'asc')
        print(".....",sort_by)
        print(".....",direction)
        search_input =self.request.GET.get('search-area') or ''
        if request.method == "GET":
            question = Question.objects.filter(title__icontains=search_input).values()
            
        if direction == 'asc':
            question = question.order_by(sort_by)
        elif direction == 'desc':
            question = question.order_by(f'-{sort_by}')
        return render(request, 'user/user_dashboard.html',{
            'questions':question,
        })
        
    
    def get_queryset(self):
        return super().get_queryset()
        
  
  

class UserProfileView(DetailView):
    model = User
    template_name = 'user/user_profile.html'
    context_object_name = 'user_profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object
        uid = user.id
        answerDetail = Answers.objects.filter(user_id=uid).values()
        askedQuestions = Question.objects.filter(user_id=uid).count()
        userQuestions = Question.objects.filter(user_id=uid).values()
        answeredUser = len(answerDetail)
        context['asked_questions'] = askedQuestions
        context['answered_user'] = answeredUser
        context['user_questions'] = userQuestions
        context['user_answers'] = answerDetail
        user_badges = User_Badges.objects.filter(user=self.object)
        badges = Badges.objects.filter(user_badges__in=user_badges).distinct()
        context['badges'] = badges
        return context


class UserUpdateView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'user/user_update.html'
    # success_url = 'user/userprofile/'

    def get_success_url(self):
        return reverse_lazy('user_profile', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_badges = User_Badges.objects.filter(user=self.object)
        badges = Badges.objects.filter(user_badges__in=user_badges).distinct()
        context['badges'] = badges
        return context



def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                domain_override='localhost:8000',
                subject_template_name='registration/password_reset_subject.txt',
                email_template_name='registration/password_reset_email.html',
                use_https=request.is_secure(),
                from_email='kvania74@gmail.com',
                request=request,
            )
            messages.success(request, 'An email has been sent with instructions to reset your password.')
    else:
        form = PasswordResetForm()
    return render(request, 'registration/password_reset_form.html', {'form': form})