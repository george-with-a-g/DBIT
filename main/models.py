from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ExtraUserInfo(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    school_id = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100, null=True)
    user_national_id_number = models.CharField(max_length=100, null=True)
    user_passport_number = models.CharField(max_length=100, null=True)

    institution_name = models.CharField(max_length=100, null=True)

    parent_first_name = models.CharField(max_length=100, null=True)
    parent_second_name = models.CharField(max_length=100, null=True)
    parent_email = models.CharField(max_length=100, null=True)
    parent_national_id_number = models.CharField(max_length=100, null=True)
    parent_passport_number = models.CharField(max_length=100, null=True)

    date_of_birth = models.DateTimeField(null=True, blank=True)
    surname = models.CharField(max_length=100, null=True)


class UserType(models.Model):#Types ranging from student, institution, educator
    type_name = models.CharField(max_length=100, null=False)
    type_description = models.CharField(max_length=1000, null=True, blank=True)

class UserTypeAllocation(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    user_type = models.ForeignKey(UserType, null=False, on_delete=models.CASCADE)

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

class UserTest(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    test_time = models.DateTimeField(auto_now_add=True)

class UserTestQuestion(models.Model):
    test = models.ForeignKey(UserTest, null=False, on_delete=models.CASCADE)
    correct_answer = models.BooleanField()



