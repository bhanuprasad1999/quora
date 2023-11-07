


from django.db.models import Q
from django.contrib.contenttypes.models import ContentType

from qa.models import Answers, Questions, Ratings


def get_ratings_count(model, object_id):
    """
    args: content_type(like, question, answer etc), object_id(question_id,)
    return rating_ count 
    """
    content_type_question = ContentType.objects.get(model=model)
    ratings = Ratings.objects.filter(Q(content_type=content_type_question, object_id=object_id))
    return len(ratings)


def get_view_of_question_and_answers(question_id):
    """
    args: questions_id
    return: {
        "question": "what is testing?",
        "answers": [
            {
                "user": "test user 1",
                "answer":"test 1"
            },
            {
                "user": "test user 2",
                "answer":"test 2"
            },
        ]
    }
    """
    try:
        question = Questions.objects.get(id = question_id)
        question.ratings = get_ratings_count('questions', question.id) 
        answers = Answers.objects.filter(question__id = question_id)
        for ans in answers:
            ans.ratings = get_ratings_count('answers', ans.id)
        print(question)
        return question, answers
    except Exception as e:
        print(e)
        return {}, []