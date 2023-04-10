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
from user.decorators import user_required
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



class QuestionDetailView(DetailView):
    model = Question
    template_name = 'ask/question_detail.html'
    context_object_name = 'question_detail'
    
    def get(self, request, *args, **kwargs):
        question = Question.objects.filter(id=self.kwargs['pk']).values()
        answer = Answers.objects.filter(question_id=self.kwargs['pk']).values()
       
        return render(request, self.template_name, {'question_detail': self.get_object(),'question':question,'answers':answer})
        
    
      
    
class QuestionDeleteView(DeleteView):
    model = Question
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/user/user/dashboard'    


# @method_decorator(login_required,name='dispatch')
@method_decorator(login_required(login_url='/user/login'), name='dispatch')
class QuestionAnswerView(CreateView):
    form_class = QuestionAnswerForm
    model = Question
    template_name = 'ask/answer_question.html'
    success_url = '/user/user/dashboard/'
    
    # def get_success_url(self):
    #     return reverse_lazy('question_detail', kwargs={'pk': self.get_object(Question.objects.all().pk)})
    
    
    def get(self, request, *args, **kwargs):
        question = Question.objects.filter(id=self.kwargs['pk']).values()
        answer = Answers.objects.filter(question_id=self.kwargs['pk']).values()
        
        return render(request, self.template_name, {'question':question,'answers':answer})


    def form_valid(self, form):
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


class TechnologyListView(ListView):
    model = TechnologyLabel
    template_name = 'ask/technology_list.html'
    context_object_name = 'technology_list'


class BadgesListView(ListView):
    model = Badges
    template_name = 'ask/badges_list.html'
    context_object_name = 'badges_list'



def like(request, answer_id):
    new_like = Answers.objects.get(user=request.user, answer_id=answer_id)
    answer = answer.likeCount + 1
    answer.save()
    return HttpResponse("Liked")
    
  