from django.contrib import admin
from .models import QuestionChoice, Question

# Register your models here.
admin.site.register(Question)
class QuestionChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice', 'correct', 'image', 'question')

admin.site.register(QuestionChoice, QuestionChoiceAdmin)
