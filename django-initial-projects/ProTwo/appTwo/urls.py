from django.urls import include, re_path
from appTwo import views

urlpatterns = [
    re_path(r'^$',views.users,name='users'),
]