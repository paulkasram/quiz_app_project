from django.contrib import admin
from django.urls import path, include
from quiz import views as quiz_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', quiz_views.index, name="index"),
    path('quiz/', include('quiz.urls')),
]
