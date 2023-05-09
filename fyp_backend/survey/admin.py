from django.contrib import admin
from .models import Survey, Question, Answer, Comment, User


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(User)
