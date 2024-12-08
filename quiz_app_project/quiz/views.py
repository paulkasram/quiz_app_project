from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import Question, QuizResult
import random

def index(request):
    return render(request, 'quiz/index.html')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Signup successful! You can log in now.")
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()

    return render(request, 'quiz/signup.html', {'form': form})


class CustomLoginView(LoginView):
    def get_success_url(self):
        return super().get_success_url()



def custom_logout(request):
    logout(request)
    return redirect('login')


@login_required
def quiz_start(request):
    # Get 5 random questions
    questions = random.sample(list(Question.objects.all()), 5)

    # Store questions in session
    request.session['quiz_questions'] = [q.id for q in questions]

    return render(request, 'quiz/quiz_start.html', {'questions': questions})


@login_required
def quiz_submit(request):
    if request.method == 'POST':
        question_ids = request.session.get('quiz_questions', [])
        score = 0
        for question_id in question_ids:
            question = Question.objects.get(id=question_id)
            user_answer = request.POST.get(f'question_{question.id}')
            print(f"Answer for {question.question_text}: {user_answer}")
            if user_answer == question.correct_option:
                score += 1

        result = QuizResult.objects.create(user=request.user, score=score)
        request.session['score'] = score
        return redirect('quiz_result')

    return HttpResponse("Invalid Request", status=400)


@login_required
def quiz_result(request):
    score = request.session.get('score', 0)
    percentage = (score / 5) * 100

    # Message based on score
    if score <= 2:
        message = "Please try again!"
    elif score == 3:
        message = "Good job!"
    elif score == 4:
        message = "Excellent work!"
    else:
        message = "You are a genius!"

    context = {
        'score': score,
        'percentage': percentage,
        'message': message
    }
    return render(request, 'quiz/quiz_result.html', context)


@login_required
def quiz_history(request):
    results = QuizResult.objects.filter(user=request.user)
    average_score = results.aggregate(avg_score=models.Avg('score'))['avg_score'] or 0
    highest_score = results.aggregate(max_score=models.Max('score'))['max_score'] or 0
    lowest_score = results.aggregate(min_score=models.Min('score'))['min_score'] or 0

    context = {
        'results': results,
        'average_score': average_score,
        'highest_score': highest_score,
        'lowest_score': lowest_score,
    }
    return render(request, 'quiz/quiz_history.html', context)


@login_required
def test_session(request):
    # Increment a session counter
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1
    return HttpResponse(f"Session counter: {request.session['counter']}")