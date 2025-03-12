from django.shortcuts import render
from .models import Question

# Create your views here.
def index(request):
    questions = Question.objects.order_by('?').all()[:5]
    context = {
        'questions' : questions
    }
    return render(request, 'main/index.html', context)

