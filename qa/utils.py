




from qa.models import Answers, Questions


def get_ratings_count(content_type, object_id):
    """
    args: content_type(like, question, answer etc), object_id(question_id,)
    return rating_ count 
    """
    pass


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
        answers = Answers.objects.filter(question__id = question_id)
        return question, answers
    except:
        return [], []