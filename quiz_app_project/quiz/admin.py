from django.contrib import admin
from .models import QuizResult, Question
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'timestamp')
    list_filter = ('user', 'score', 'timestamp')
    search_fields = ('user__username', 'score')
    ordering = ('-timestamp',)
    date_hierarchy = 'timestamp'

admin.site.register(QuizResult, QuizResultAdmin)


class QuizResultInline(admin.TabularInline):
    model = QuizResult
    extra = 0


class CustomUserAdmin(UserAdmin):
    inlines = [QuizResultInline]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'option_1', 'option_2', 'option_3', 'option_4', 'correct_option')
    search_fields = ('question_text', 'correct_option')
    list_filter = ('correct_option',) 
    fieldsets = (
        ('Question Details', {
            'fields': ('question_text',)
        }),
        ('Options', {
            'fields': ('option_1', 'option_2', 'option_3', 'option_4')
        }),
        ('Correct Answer', {
            'fields': ('correct_option',)
        }),
    )

admin.site.register(Question, QuestionAdmin)