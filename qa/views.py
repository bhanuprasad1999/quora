from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType

from qa.forms import AnswerForm, QuestionForm
from qa.models import Questions, Ratings
from qa.utils import get_view_of_question_and_answers



def add_question(request):
    if not request.user.is_authenticated:
        return redirect('/user/login/')
    form = QuestionForm(request.POST)
    logged_in = request.user

    if form.is_valid():
        form.instance.user_id = logged_in
        instance = form.save()
        return redirect(f'/qa/view_question/{instance.id}')

    else:
        form = QuestionForm()
    return render(request, 'add_question.html', {'question_form':form})


def update_question(request, question_id):
    if not request.user.is_authenticated:
        return redirect('/user/login/')
    question = Questions.objects.get(id=question_id)
    form = QuestionForm(request.POST, instance=question)
    logged_in = request.user

    if form.is_valid():
        form.instance.user_id = logged_in
        instance = form.save()
        return redirect(f'/qa/view_question/{instance.id}')

    else:
        form = QuestionForm(instance=question)
    return render(request, 'update_question.html', {'question_form':form})


def list_questions(request):
    questions = Questions.objects.all()
    return render(request, 'questions_list.html', {'questions':questions})


def submit_answer_for_question(request, question_id):
    form = AnswerForm(request.POST)
    if form.is_valid():
        form.instance.user_id = request.user
        form.instance.question = Questions.objects.get(id=question_id)
        form.save()
    return redirect(f'/qa/view_question/{question_id}')



def view_question_and_answer(request, id):
    question_prev, answers = get_view_of_question_and_answers(id)
    if not question_prev:
        return redirect('/page_not_found/')
    form = AnswerForm()
    return render(request, 'preview_question.html', {'question':question_prev, 'answers':answers, 'form':form })



def vote_for_question(request, question_id):
    if not request.user.is_authenticated:
        return redirect('/user/login/')
    redirect_path = request.META.get('HTTP_REFERER', '/')
    content_type_question = ContentType.objects.get(model='questions')
    ratings_for_question = Ratings.objects.filter(Q(content_type=content_type_question, object_id=question_id, user_id=request.user))

    if len(ratings_for_question) == 0:
        rating = Ratings(vote=True)
        rating.content_type = content_type_question
        rating.object_id = question_id
        rating.user_id = request.user
        rating.save()
    return redirect(redirect_path)
    


def vote_for_answer(request, answer_id):
    if not request.user.is_authenticated:
        return redirect('/user/login/')
    redirect_path = request.META.get('HTTP_REFERER', '/')
    content_type_answer = ContentType.objects.get(model='answers')
    ratings_for_answer = Ratings.objects.filter(Q(content_type=content_type_answer, object_id=answer_id, user_id=request.user))
 
    if len(ratings_for_answer) == 0:
        rating = Ratings(vote=True)
        rating.content_type = content_type_answer
        rating.object_id = answer_id
        rating.user_id = request.user
        rating.save()
    return redirect(redirect_path)

