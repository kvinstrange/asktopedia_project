from django.shortcuts import render
from django.views.generic import CreateView
from .forms import *
from django.views.generic import ListView,DetailView
from django.views.generic import DeleteView,UpdateView
from .models import *
# Create your views here.


def home(request):
    return render(request,"home.html")


class AskQuestionView(CreateView):
    form_class = AskQuestionForm
    model = Question
    template_name = 'ask/question_create.html'
    success_url = '/ask/list_question/'
    
    
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



# class QuestionDetailView(DetailView):
#     model = Question
#     template_name = 'ask/question_detail.html'
#     context_object_name = '_detail'
    
#     def get(self, request, *args, **kwargs):
#         team = ProjectTeam.objects.filter(Project_id=self.kwargs['pk'])
#         return render(request, self.template_name, {'project_detail': self.get_object(),'team':team})
    
      
    
class QuestionDeleteView(DeleteView):
    model = Question
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/ask/list_question/'    
