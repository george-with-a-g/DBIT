from django.shortcuts import render
from .models import Question

# Create your views here.
def index(request):
    questions = Question.objects.order_by('?').all()[:5]
    context = {
        'questions' : questions
    }
    return render(request, 'main/index.html', context)

def signupold(request):
    return render(request, 'main/authentication/index.html')

def loginold(request):
    return render(request, 'main/authentication/login.html')

def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        surname = request.POST.get('surname')
        lastname = request.POST.get('lastname')
        dateofbirth = request.POST.get('dob')
        education = request.POST.get('education')
        accounttype = request.POST.getlist('accounttype[]')
        print(f"Email is {email}, First Name is {firstname}, Surname is {surname} and Last Name is {lastname} and date of birth is {dateofbirth}")
        print(f"Education is {education} and accounttype is {accounttype}.")
        print(request.POST)
        print(accounttype)
        print("###########################################")
    return render(request, 'main/authentication/signup2.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Username is {username} and password is {password}")
    return render(request, 'main/authentication/login2.html')

def auth(request):
    if request.method == "POST":
        signup_form_firstname = request.POST.get('Sign-Up-Form-FirstName')
        signup_form_surname = request.POST.get('Sign-Up-Form-SurName')
        signup_form_lastname = request.POST.get('Sign-Up-Form-LastName')
        signup_form_email = request.POST.get('Sign-up-Form-4-Email')
        signup_form_password = request.POST.get('Sign-up-Form-4-Password')

        login_form_email = request.POST.get('Log-in-Form-4-Email')
        login_form_password = request.POST.get('Log-in-Form-4-Password')
        if login_form_email == None and login_form_password == None:
            print(f"SignUp Email- {signup_form_email}. SignUp Password- {signup_form_password}. SignUp First Name- {signup_form_firstname}. SignUp SurName- {signup_form_surname}. SignUp LastName- {signup_form_lastname}.")
        else:
            print(f"Login Email- {login_form_email}. Login Password- {login_form_password}")


    return render(request, 'main/authentication/index.html')

