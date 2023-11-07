from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User

# Create your models here.
class Questions(models.Model):
    id = models.BigAutoField(unique=True, primary_key=True, null=False, blank=False)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)
    question_title = models.CharField(max_length=300, null=False, blank=False)
    question_description = models.TextField()

    class Meta:
        db_table = 'questions'



class Answers(models.Model):
    id = models.BigAutoField(unique=True, primary_key=True, null=False, blank=False)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, null=False, blank=False)
    answer = models.TextField()

    class Meta:
        db_table = 'answers'


class Ratings(models.Model):
    id = models.BigAutoField(unique=True, primary_key=True, null=False, blank=False)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)
    vote = models.BooleanField(default=0)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in':['questions', 'answers']})
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")


    class Meta:
        db_table = 'ratings'

