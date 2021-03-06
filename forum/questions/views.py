import re
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Question, Answer, Tag
from django.http import HttpResponse, HttpResponseRedirect
from .forms import DisplayForm, NewCommentForm
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView
from django.contrib.auth import authenticate, login
from django.urls import reverse, reverse_lazy
from .forms import NewCommentForm
from django.views.generic.edit import FormMixin, ModelFormMixin
from django.contrib.messages.views import SuccessMessageMixin





class IndexView(ListView):
     template_name = 'questions/index.html'
     context_object_name = 'questions'

     def get_queryset(self):
         return Question.objects.all()


class AskView(CreateView):
    template_name = 'questions/ask.html'
    queryset = Question.objects.all()
    form_class = DisplayForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        tags = form.cleaned_data['tags'].lower()

        question_tags = re.split("\s", tags)

        for eachtag in question_tags:
            tag, created = Tag.objects.get_or_create(
                name=eachtag)
            tag.save()
            instance.tags.add(tag)
        form.save_m2m()

        return HttpResponseRedirect(
            reverse('questions:id', kwargs={'id':instance.id}))

    def get_context_data(self, **kwargs):

        context = super(AskView, self).get_context_data(**kwargs)
        tags_list = [tag for tag in
                     Tag.objects.values_list('name', flat=True)]
        tags_string = ''
        quote = '"'
        for tag in tags_list:
            tags_string += quote + tag + quote + ","
        context['tags'] = tags_string
        return context
    










    # model = Question
    # def post(self, request):
    #     form = DisplayForm(request.POST):
    #     if form.is_valid():
    #         tags = form.get('tags')
    #         tags = tags.split()
    #         for tag in tags:
    #             if Tag.objects.filter(name=tag).exists():



    # def get_success_url(self):
    #     return reverse('questions:id', kwargs={'id':self.object.id})    



class QuestionDetailView(ModelFormMixin, DetailView):
    template_name = 'questions/question_detail.html'
    context_object_name = 'question'
    form_class = NewCommentForm
    model = Question
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        id_ = self.get_object().id
        answers = Answer.objects.filter(question_id=id_)
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        context["answers"] = answers
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # my_form = self.get_form()
        my_form = NewCommentForm(request.POST or None)
        if my_form.is_valid():
            obj = my_form.save(commit=False)
            obj.author = request.user
            obj.question_id = Question.objects.get(id=id)
            my_form.save()
            return self.form_valid(my_form)
        else:
            return self.form_invalid(my_form)

    def get_success_url(self):
        return reverse('questions:id', kwargs={'id':self.get_object().id})         




class LikeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        id_ = self.kwargs.get('id')
        obj = get_object_or_404(Question, id=id_)
        user = self.request.user
        url = obj.get_absolute_url()
        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user) 
        return url 



class UpdateQuestionView(UpdateView):
    template_name = 'questions/ask.html'
    queryset = Question.objects.all()
    form_class = DisplayForm
    # model = Question
    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Question, id=id_)

    def get_success_url(self):
        return reverse('questions:id', kwargs={'id':self.object.id})



class DeleteQuestion(DeleteView):
    template_name = 'questions/delete.html'
    queryset = Question.objects.all()
    
    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Question, id=id_)

    success_url = reverse_lazy('questions:all_questions')
        

class EditAnswer(UpdateView):
    pass

class DeleteAnswer(DeleteView):
    pass

class AnswerView(CreateView):
    # template_name = 'questions/question_detail.html'
    pass



class AnswerView(CreateView):
    pass        


class TagView(CreateView):
    pass


def about_us(request):
    return HttpResponse("this is about us")

def contact(request):
    return HttpResponse("contact page")    


#def index(request):

#   questions = models.Question.objects.filter(status='published')
#   context = {'questions':questions}
#   return render(request, 'questions/index.html', context)

        
# def get_context_data(self, **kwargs):
#     # Call the base implementation first to get the context
#     context = super(IndexView, self).get_context_data(**kwargs)
#     # Create any data and add it to the context
#     # context['some_data'] = 'This is just some data'
#     return context
    


# def ask_question(request):

#     if request.method == "POST":
#         form = DisplayForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("../")

#     else:
#         form = DisplayForm()    

#     return render(request, 'questions/ask.html', {'form':form})    




# def question_detail(request, q_id):

#     question = Question.objects.get(id=q_id)
#     answers = question.answer_set.all() #answer_set is the related name for the questions_id foreign key in Answer table

#     context = {
#         'question':question,
#         'answers':answers,
#     }

#     return render(request, 'questions/question_detail.html', context)

# class AnswerLikeView(RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         id_ = self.kwargs.get('id')
#         obj = get_object_or_404(Question, id=id_)
#         user = self.request.user
#         url = obj.get_absolute_url()
#         if user.is_authenticated:
#             if user in obj.likes.all():
#                 obj.likes.remove(user)
#             else:
#                 obj.likes.add(user) 
#         return url 
        
  # def post(self, request, *args, **kwargs):
    #     print('test')
    #     self.object = self.get_object()
    #     print('test')
    #     form = self.get_form()
    #     print('test')
    #     if form.is_valid():
    #         print('test valid')
    #         return self.form_valid(form)
    #         print('validated')
    #     else:
    #         return self.form_invalid(form)

    # def form_valid(self, form):
    #     answer = form.save(commit=False)
    #     answer.created_by = self.request.user
    #     answer.post = self.object
    #     answer.save()
    #     return super(QuestionDetailView, self).form_valid(form)      









    # def create_answer(self, request, *args, **kwargs):
    #     new_answer = Answer(content=request.POST.get('content'),
    #                         author=self.request.user,
    #                         question_id=self.get_object())   
    #     new_answer.save() 

    #     return self.get(self, request, *args, **kwargs)    

    # def get_success_url(self):
    #     return reverse('questions:id', kwargs={'id':self.object.id})                      
