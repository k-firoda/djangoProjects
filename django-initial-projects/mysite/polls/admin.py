from django.contrib import admin

# Register your models here.
from .models import Choice, Question

# admin.site.register(Question)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # inlines = [ChoiceInline]
    list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)