from django.urls import path

from . import views

app_name = 'basicapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.form_name_view, name='form_name'),
    
]