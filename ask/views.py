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
    
    
    # def get(self, request, *args, **kwargs):
    #     question = Question.objects.filter(id=self.kwargs['pk']).values()
    #     answer = Answers.objects.filter(question_id=self.kwargs['pk']).values()
        
    #     return render(request, self.template_name, {'question':question,'answers':answer})


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



def like(request):
    # anslike = get_object_or_404(Answers, pk=anslike_id)
    # user = request.user
    # if Like.objects.filter(user=user, anslike=anslike).exists():
    #     return HttpResponseBadRequest("You have already liked this post.")
    # else:
    #     Like.objects.create(user=user, anslike=anslike)
    #     return redirect('post_detail', pk=anslike.pk)


     # def save(self, *args, **kwargs):
    #     if self.pk:  # check if the instance has already been saved
    #         old_instance = Answers.objects.get(pk=self.pk)
    #         if self.likeCount != old_instance.likeCount:
    #             raise ValidationError("You cannot change the like count for this instance.")
    #     super(Answers, self).save(*args, **kwargs)


    user = request.user
    print(user)
    answerDetail = Answers.objects.all().values()
    answerDetail1 = Answers.objects.filter(user_id =user.id)
    print(answerDetail1)

   
    id = request.GET.get('id')
    print("id.....",id)
    new_like = Answers.objects.get(id=id)
    questdetail = Answers.objects.filter(id=id).values('question_id')
    qid =questdetail[0].get('question_id')
    # print(new_like)
    prvlikecount = new_like.likeCount
    # print(prvlikecount)
    updatedCount = prvlikecount+1
    # print(updatedCount)
    new_like.likeCount =updatedCount
    new_like.save()
    # messages.success(request, 'You have liked the post!')
    #answer = answer.likeCount + 1
    #answer.save()
    return redirect('detail_question',qid)




def dislike(request):
    id = request.GET.get('id')
    print("id.....",id)
    new_like = Answers.objects.get(id=id)
    questdetail = Answers.objects.filter(id=id).values('question_id')
    qid =questdetail[0].get('question_id')
    prvlikecount = new_like.dislikeCount
    updatedCount = prvlikecount+1
    new_like.dislikeCount =updatedCount
    new_like.save()
    return redirect('detail_question',qid)
    
  