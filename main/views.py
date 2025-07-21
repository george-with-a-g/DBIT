from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Question, ExtraUserInfo, UserType, UserTypeAllocation
from datetime import datetime
from django.utils import timezone

# Create your views here.
@login_required(login_url='auth-login')
def index(request):
    questions = Question.objects.order_by('?').all()[:5]
    context = {
        'questions' : questions
    }
    return render(request, 'main/index.html', context)

def dashboard(request):
    return render(request, 'main/dashboard/dashboard.html')

def signupold(request):
    return render(request, 'main/authentication/index.html')

def logout_view(request):
    auth_logout(request)
    return redirect('auth-login')

def loginold(request):
    return render(request, 'main/authentication/login.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('main')

    if request.method == "POST":
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        surname = request.POST.get('surname')
        lastname = request.POST.get('lastname')

        dateofbirth = request.POST.get('dob')
        date_format = "%Y-%m-%d"
        parsed_datetime = datetime.strptime(dateofbirth, date_format)
        parsed_datetime = timezone.make_aware(parsed_datetime)

        education = request.POST.get('education')
        accounttype = request.POST.getlist('accounttype[]')
        password = request.POST.get('password')

        # Create a new user
        try:
            # Create a username from email (or use email as username)
            username = email
            # Create the user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=firstname,
                last_name=lastname
            )
            # You can add additional user info to your ExtraUserInfo model here
            extra_info = ExtraUserInfo(user=user, date_of_birth=parsed_datetime, surname=surname)
            extra_info.save()

            if len(accounttype) == 1:
                account_type_object = UserType.objects.filter(type_name=accounttype[0]).first()
                account_allocation = UserTypeAllocation(user=user, user_type=account_type_object)
                account_allocation.save()
                # print(f"Single Account Type: {account_type_object.type_name}.")
            elif len(accounttype) > 1:
                accounttype_count = 0
                while accounttype_count < len(accounttype):
                    account_type_object = UserType.objects.filter(type_name=accounttype[accounttype_count]).first()
                    account_allocation = UserTypeAllocation(user=user, user_type=account_type_object)
                    account_allocation.save()
                    # print(f"{accounttype_count + 1}. {account_type_object.type_name}.")
                    accounttype_count += 1

            # Log the user in
            auth_login(request, user)
            return redirect('main')
        except Exception as e:
            context = {
                'error_message': f'Error creating account: {str(e)}'
            }
            print(context)
            return render(request, 'main/authentication/signup2.html', context)
    return render(request, 'main/authentication/signup2.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('main')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # User is authenticated, log them in
            auth_login(request, user)
            return redirect('main')  # Redirect to home page after login
        else:
            # Authentication failed
            context = {
                'error_message': 'Invalid username or password.'
            }
            return render(request, 'main/authentication/login2.html', context)
            
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
        
        if login_form_email is None and login_form_password is None:
            # This is a signup request
            try:
                # Create user
                user = User.objects.create_user(
                    username=signup_form_email,
                    email=signup_form_email,
                    password=signup_form_password,
                    first_name=signup_form_firstname,
                    last_name=signup_form_lastname
                )
                
                # Log the user in
                auth_login(request, user)
                return redirect('main')
                
            except Exception as e:
                context = {
                    'error_message': f'Error creating account: {str(e)}'
                }
                return render(request, 'main/authentication/index.html', context)
        else:
            # This is a login request
            user = authenticate(request, username=login_form_email, password=login_form_password)
            
            if user is not None:
                # User is authenticated, log them in
                auth_login(request, user)
                return redirect('main')
            else:
                # Authentication failed
                context = {
                    'error_message': 'Invalid email or password.'
                }
                return render(request, 'main/authentication/index.html', context)

    return render(request, 'main/authentication/index.html')

def log_test_score(request):
    return JsonResponse({"work":"success"})
