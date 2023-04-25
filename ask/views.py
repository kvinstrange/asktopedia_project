from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView
from .forms import *
from django.views.generic import ListView,DetailView
from django.views.generic import DeleteView,UpdateView
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Answers
from .models import Question
from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest
from django.contrib import messages
from django import template
from datetime import datetime
from django.core.mail import send_mail
from django.contrib.auth import get_user_model


# Create your views here.

def home(request):
    return render(request,"home.html")



# @method_decorator(login_required, name='dispatch')
@method_decorator(login_required(login_url='/user/login'), name='dispatch')
class AskQuestionView(CreateView):
    form_class = AskQuestionForm
    model = Question
    template_name = 'ask/question_ask.html'
    success_url = '/user/user/dashboard/'
    
    def form_valid(self, form):
        user = self.request.user
        print("................",user)
        instance = form.save(commit=False)
        instance.user = user
        instance.save()
        return super().form_valid(form)
    


class QuestionListView(ListView):
    model = Question
    template_name = 'ask/question_list.html'
    context_object_name = 'question_list'
    
    def get_queryset(self):
        return super().get_queryset()    
    
    
    


class QuestionUpdateView(UpdateView):
    model = Question
    form_class = AskQuestionForm
    template_name = 'ask/question_create.html'
    success_url = '/ask/list_question/'



class QuestionDeleteView(DeleteView):
    model = Question
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/user/user/dashboard'  



@method_decorator(login_required(login_url='/user/login'), name='dispatch')
class QuestionDetailView(DetailView):
    model = Question
    template_name = 'ask/question_detail.html'
    context_object_name = 'question_detail'
    
    def get(self, request, *args, **kwargs):
        question = Question.objects.filter(id=self.kwargs['pk']).values()
        answer = Answers.objects.filter(question_id=self.kwargs['pk']).values()
        return render(request, self.template_name, {'question_detail': self.get_object(),'question':question,'answers':answer})

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     question = Question.objects.filter(id=self.kwargs['pk']).values()
    #     answer = Answers.objects.filter(question_id=self.kwargs['pk']).values()
    #     context['question'] = question
    #     context['answers'] = answer
    #     # context['answer_form'] = QuestionAnswerForm(initial={'question': question.id})
    #     return context  
    

  

@method_decorator(login_required(login_url='/user/login'), name='dispatch')
class QuestionAnswerView(CreateView):
    form_class = QuestionAnswerForm
    model = Question
    template_name = 'ask/answer_question.html'
    success_url = '/user/user/dashboard/'
    
    # def get_success_url(self):
    #     return reverse_lazy('detail_question', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = get_object_or_404(Question, id=self.kwargs['pk'])
        context['answers'] = Answers.objects.filter(question_id=self.kwargs['pk'])
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['question_pk'] = self.kwargs['pk']
        return kwargs

    def form_valid(self, form):
        user = self.request.user
        print("................",user)
        instance = form.save(commit=False)
        instance.user = user
        instance.question_id = self.kwargs['pk']
        instance.save()
        return super().form_valid(form) 




class AnswerView(View):
    def get(self, request, *args, **kwargs):
         view = QuestionDetailView.as_view()
         return view(request, *args, **kwargs) 

    def post(self, request, *args, **kwargs) :
         view = QuestionAnswerView.as_view()
         return view(request, *args, **kwargs) 





class AnswerUpdateView(UpdateView):
    model = Answers
    form_class = QuestionAnswerForm
    template_name = 'ask/answer_question.html'
    success_url = '/user/user/dashboard/'




class AnswerDeleteView(DeleteView):
    model = Answers
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/user/user/dashboard/' 



@method_decorator(login_required(login_url='/user/login'), name='dispatch')
class TechnologyListView(ListView):
    model = TechnologyLabel
    template_name = 'ask/technology_list.html'
    context_object_name = 'technology_list'



@method_decorator(login_required(login_url='/user/login'), name='dispatch')
class BadgesListView(ListView):
    model = Badges
    template_name = 'ask/badges_list.html'
    context_object_name = 'badges_list'



def like(request):
    user = request.user
    print("Logged in user----------",user)
    uid = user.id
    answerDetail = Answers.objects.filter(user_id =user.id).values()
    # print("Answers of user-----------",answerDetail2)
    answeredUser = len(answerDetail)
    print("Total answers................",answeredUser)
    badges = Badges.objects.all().values()
    
   
    id = request.GET.get('id')
    print("answer id.....",id)
    new_like = Answers.objects.get(id=id)   
    questdetail = Answers.objects.filter(id=id).values('question_id')
    qid =questdetail[0].get('question_id')
    print('Answer to like----------',new_like)
    prvlikecount = new_like.likeCount

    user_likes = User_Like.objects.filter(user=user, answer=new_like)
    if user_likes.exists():
        messages.warning(request, "You have already liked this answer.")
        return redirect('detail_question', qid)

    if prvlikecount>0:
        if answeredUser >= 2:
            badge_id = badges[1].get('id') 
            print("Bronze.........",badge_id)
            user_badges = User_Badges(user_id=uid, badge_id=badge_id)
            print("User.........",user_badges)
            user_badges.save()

        if answeredUser >= 4:
            badge_id = badges[0].get('id') 
            print("Silver.........",badge_id)
            user_badges = User_Badges(user_id=uid, badge_id=badge_id)
            print(user_badges)
            user_badges.save()

        if answeredUser >= 6:
            badge_id = badges[2].get('id') 
            print("Gold.........",badge_id)
            user_badges = User_Badges(user_id=uid, badge_id=badge_id)
            print(user_badges)
            user_badges.save()

    print("OLd likes------",prvlikecount)
    updatedCount = prvlikecount+1
    print("New likes---------",updatedCount)
    new_like.likeCount =updatedCount
    new_like.save()

    User_Like.objects.create(user=user, answer=new_like)
    return redirect('detail_question',qid)




def dislike(request):
    user = request.user
    id = request.GET.get('id')
    print("id.....",id)
    new_like = Answers.objects.get(id=id)
    questdetail = Answers.objects.filter(id=id).values('question_id')
    qid =questdetail[0].get('question_id')
    prvlikecount = new_like.dislikeCount

    user_likes = User_Like.objects.filter(user=user, answer=new_like)
    if user_likes.exists():
        # User has already liked this answer
        messages.warning(request, "You have already disliked this answer.")
        return redirect('detail_question', qid)
    
    updatedCount = prvlikecount+1
    new_like.dislikeCount =updatedCount
    new_like.save()
    User_Like.objects.create(user=user, answer=new_like)
    return redirect('detail_question',qid)
    
  


def contactUs(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail( 
            'Thank you for contacting us.', #title
            'You have a new message from Asktopedia and you will be shortly informed regarding '+
            subject,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False  

        )


    return redirect('http://127.0.0.1:8000/')


def subscribe(request):
    if request.method == 'POST':
        message = 'Thank you for connecting with us. You will get notified about all the updates of the Asktopedia website.'
        email = request.POST['email']

        send_mail( 
            'Subscription of Asktopedia', #title
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False  

        )

        messages.info(request,'Your message has been send successfully .')

    return redirect('http://127.0.0.1:8000/')