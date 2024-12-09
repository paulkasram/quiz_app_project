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
    questions = random.sample(list(Question.objects.all()), 5)
    request.session['quiz_questions'] = [q.id for q in questions]
    return render(request, 'quiz/quiz_start.html', {'questions': questions})


@login_required
def quiz_submit(request):
    if request.method == 'POST':
        try:
            question_ids = request.session.get('quiz_questions', [])
            score = 0
            for question_id in question_ids:
                question = Question.objects.get(id=question_id)
                user_answer = request.POST.get(f'question_{question.id}')
                if user_answer == question.correct_option:
                    score += 1

            result = QuizResult.objects.create(user=request.user, score=score)
            request.session['score'] = score
            request.session.pop('quiz_questions', None)
            return redirect('quiz_result')

        except Question.DoesNotExist:
            messages.error(request, "An error occurred while fetching the question.")
            return redirect('quiz_start')
    
        except Exception as e:
            messages.error(request, f"Unexpected error: {str(e)}")
            return redirect('quiz_start')

    return HttpResponse("Invalid Request", status=400)


@login_required
def quiz_result(request):
    score = request.session.get('score', 0)
    percentage = (score / 5) * 100

    score_messages = {
        range(0, 3): "Please try again!",
        range(3, 4): "Good job!",
        range(4, 5): "Excellent work!",
        range(5, 6): "You are a genius!"
    }

    message = "Unexpected score"
    for score_range, msg in score_messages.items():
        if score in score_range:
            message = msg
            break

    user_avg_score = QuizResult.objects.filter(user=request.user).aggregate(models.Avg('score'))['score__avg'] or 0
    comparison_message = "Your score is above average!" if score >= user_avg_score else "Keep practicing to beat your average!"

    badges = []
    if score == 5:
        badges.append("Master")
    elif score == 4:
        badges.append("High Achiever")
    elif score == 3:
        badges.append("Good Job")

    scores = QuizResult.objects.filter(user=request.user).order_by('timestamp').values_list('score', flat=True)

    context = {
        'score': score,
        'percentage': percentage,
        'message': message,
        'user_avg_score': user_avg_score,
        'comparison_message': comparison_message,
        'badges': badges,
    }

    return render(request, 'quiz/quiz_result.html', context)


@login_required
def quiz_history(request):
    results = QuizResult.objects.filter(user=request.user).select_related('user')
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
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1
    return HttpResponse(f"Session counter: {request.session['counter']}")
