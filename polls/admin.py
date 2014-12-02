from django.contrib import admin
from polls.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display=('question_text','pub_date', 'was_published_recently')
    fieldsets = [
        ('Preguntita de marras',               {'fields': ['question_text']}),
        ('Cuando Cuando', {'fields': ['pub_date'],'classes': ['collapse']}),
    ]
    inlines= [ChoiceInline]
    list_filter=["pub_date"]
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

# Register your models here.
