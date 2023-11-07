from django.shortcuts import render, redirect

from qa.forms import AnswerForm, QuestionForm
from qa.models import Questions
from qa.utils import get_view_of_question_and_answers



def add_question(request):
    form = QuestionForm(request.POST)
    logged_in = request.user
    print(logged_in)
    if form.is_valid():
        form.instance.user_id = request.user
        instance = form.save()
        return redirect(f'/qa/view_question/{instance.id}')

    else:
        form = QuestionForm()
    return render(request, 'add_question.html', {'question_form':form})


def update_question():
    pass

def list_questions():
    pass


def submit_answer_for_question(request, question_id):
    form = AnswerForm(request.POST)
    logged_in = request.user
    print(logged_in)
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


