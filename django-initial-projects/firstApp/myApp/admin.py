from django.contrib import admin
from myApp.models import Topic, Question, Webpage, AccessRecord
# Register your models here.

admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
