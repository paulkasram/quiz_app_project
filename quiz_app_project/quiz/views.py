from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Question, QuizResult
import random

def index(request):
    return render(request, 'quiz/index.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('quiz_home')  # Redirect to quiz home page
    else:
        form = UserCreationForm()
    return render(request, 'quiz/signup.html', {'form': form})


@login_required
def start_quiz(request):
    # Select 5 random questions
    questions = list(Question.objects.all())
    random_questions = random.sample(questions, 5)
    
    # Store question IDs in the session for later use
    request.session['quiz_questions'] = [q.id for q in random_questions]
    request.session['score'] = 0  # Initialize score
    
    return render(request, 'quiz/quiz_start.html', {'questions': random_questions})


@login_required
def submit_quiz(request):
    if request.method == 'POST':
        # Retrieve selected answers and stored question IDs
        question_ids = request.session.get('quiz_questions', [])
        score = 0

        for question_id in question_ids:
            question = Question.objects.get(id=question_id)
            user_answer = request.POST.get(f'question_{question.id}')

            # Check if the user's answer matches the correct option
            if user_answer == question.correct_option:
                score += 1

        # Save the result to the database
        QuizResult.objects.create(user=request.user, score=score)

        # Store the final score in session
        request.session['score'] = score

        return redirect('quiz_result')

    return HttpResponse("Invalid Request", status=400)


@login_required
def quiz_result(request):
    score = request.session.get('score', 0)
    percentage = (score / 5) * 100

    # Determine message based on score
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
    # Fetch all quiz results for the logged-in user
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

