from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.CustomLoginView.as_view(template_name='quiz/login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('start/', views.quiz_start, name='quiz_start'),
    path('submit/', views.quiz_submit, name='quiz_submit'),
    path('result/', views.quiz_result, name='quiz_result'),
    path('history/', views.quiz_history, name='quiz_history'),

    path('test-session/', views.test_session, name='test_session'),
]
