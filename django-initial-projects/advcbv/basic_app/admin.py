from django.contrib import admin

# Register your models here.
from django.contrib import admin
from basic_app.models import School,Student
# Register your models here.
admin.site.register(School)
admin.site.register(Student)
