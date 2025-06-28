from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('auth/', views.auth, name='auth'),
    path('auth/signup/old/', views.signupold, name='auth-signup-old'),
    path('auth/login/old/', views.login, name='auth-login-old'),

    path('auth/signup/', views.signup, name='auth-signup'),
    path('auth/login/', views.login, name='auth-login'),
    path('auth/logout/', views.logout_view, name='auth-logout'),

]
