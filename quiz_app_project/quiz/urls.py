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
    path('add-question/', views.add_question, name='add_question'),
    path('question-list/', views.question_list, name='question_list'),
    path('access_denied/', views.access_denied, name='access_denied'),
    path('test-session/', views.test_session, name='test_session'),
]
