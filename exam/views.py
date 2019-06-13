from django.shortcuts import render

# Create your views here.

from exam.models import *
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from exam.forms import *
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return redirect('exam:home')


@login_required
def home(request):
    import pdb
    # pdb.set_trace()
    print (request)
    name = "prashanth"
    date = datetime.datetime.now()

    # return HttpResponse("<h1>Hello %s, Time is %s</h1>" % (name, str(date)))
    return render(request, 'exam/home.html', {'name': name, 'date1': date})


@login_required
def contact(request):
    context = {'contact': 9959994410}
    return render(request, 'exam/contact.html', context)


@login_required
def about(request):
    context = {'info': 'This is the job providing website'}
    return render(request, 'exam/about.html', context)


@login_required
def questions_list(request):
    # import pdb; pdb.set_trace()
    if request.method == 'GET':
        questions = Question.objects.all()
        return render(request, 'exam/question-list.html',
                      {'questions': questions})
    return redirect('exam:home')


@login_required
def delete_question(request, id=None):
    if request.method == 'POST':
        question_obj = Question.objects.filter(id=id).first()
        if question_obj:
            # question_obj.delete()
            return JsonResponse({'success': True,
                                 "message": "Question deleted successufully."})
        return JsonResponse({'success': False,
                             "message": "Question Not Found."})
    return redirect('exam:home')


@login_required
def create_question(request):
    if request.method == 'GET':
        # import pdb; pdb.set_trace()
        question_create_form = QuestionForm()
        return render(request, 'exam/create_question.html',
                      {'question_create_form': question_create_form})

    elif request.method == 'POST':
        question_create_form = QuestionForm(request.POST)
        if question_create_form.is_valid():
            question_obj = question_create_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Question Created Successfully!.')
            return redirect(reverse('exam:update_question', kwargs={'id': question_obj.id}))
        else:
            messages.add_message(request, messages.ERROR,
                                 'Something Went Wrong!.')
            return render(request, 'exam/create_question.html',
                          {'question_create_form': question_create_form})
        return redirect('exam:home')


@login_required
def update_question(request, id):
    question_obj = Question.objects.filter(id=id).first()
    if not question_obj:
        messages.add_message(request, messages.ERROR,
                             'Question not found!.')
        return redirect('exam:questions_list')
    if request.method == 'GET':
        question_update_form = QuestionForm(instance=question_obj)
        return render(request, 'exam/update_question.html',
                      {'question_update_form': question_update_form})
    elif request.method == 'POST':
        question_update_form = QuestionForm(
            request.POST, instance=question_obj)
        if question_update_form.is_valid():
            question_obj = question_update_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Question Updated Successfully!.')
            return redirect(reverse('exam:update_question', kwargs={'id': question_obj.id}))
        else:
            messages.add_message(request, messages.ERROR,
                                 'Something Went Wrong!.')
            return render(request, 'exam/update_question.html',
                          {'question_update_form': question_update_form})
    return redirect('exam:questions_list')
