from django.shortcuts import render
from .models import Question

# Create your views here.
def index(request):
    questions = Question.objects.order_by('?').all()[:5]
    context = {
        'questions' : questions
    }
    return render(request, 'main/index.html', context)

def auth(request):
    if request.method == "POST":
        signup_form_firstname = request.POST.get('Sign-Up-Form-FirstName')
        signup_form_surname = request.POST.get('Sign-Up-Form-SurName')
        signup_form_lastname = request.POST.get('Sign-Up-Form-LastName')
        signup_form_email = request.POST.get('Sign-up-Form-4-Email')
        signup_form_password = request.POST.get('Sign-up-Form-4-Password')

        login_form_email = request.POST.get('Log-in-Form-4-Email')
        login_form_password = request.POST.get('Log-in-Form-4-Password')


    return render(request, 'main/authentication/index.html')

