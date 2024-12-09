from django.contrib import admin
from .models import QuizResult
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

