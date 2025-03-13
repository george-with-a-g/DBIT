from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=400, null=True, blank=True)
    def __str__(self):
        return f"{self.name}"

class Topic(models.Model):
    name = models.CharField(max_length=400, null=True, blank=True)
    def __str__(self):
        return f"{self.name}"

class Question(models.Model):
    question = models.CharField(max_length=400, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.question}"

class QuestionChoice(models.Model):
    choice = models.CharField(max_length=400)
    correct = models.BooleanField(default=False)
    image = models.ImageField(upload_to='choiceimage/', blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

