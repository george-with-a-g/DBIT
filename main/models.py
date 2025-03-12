from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=400, null=True, blank=True)

class QuestionChoice(models.Model):
    choice = models.CharField(max_length=400)
    correct = models.BooleanField(default=False)
    image = models.ImageField(upload_to='choiceimage/', blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

