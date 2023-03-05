from django.shortcuts import render, get_object_or_404
from forum.models import *

# Create your views here.

def create_question(request):
    
    context = {}

    if request.method == 'POST':
        author = request.POST.get('author')
        title = request.POST.get('title')
        text = request.POST.get('text')

        Question.objects.create(author=author, title = title, text = text)
        context['success_text'] = 'Ваше запитання створено.' 
        
    return render(request, 'create_question.html', context = context)

def show_question(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    
    if request.method == 'POST':
        author = request.POST.get('author')
        text = request.POST.get('text')
        Answer.objects.create(author=author, text=text, question_id = question_pk)
    answers = Answer.objects.filter(question_id = question_pk)
    return render(request, 'question.html', context = {'question': question, 'answers': answers})

def show_main_page(request):
    return render(request, 'main_page.html', context = {'question': Question.objects.all()})