from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='quiz/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('start/', views.start_quiz, name='quiz_start'),
    path('submit/', views.submit_quiz, name='quiz_submit'),
    path('result/', views.quiz_result, name='quiz_result'),
    path('history/', views.quiz_history, name='quiz_history'),
]
