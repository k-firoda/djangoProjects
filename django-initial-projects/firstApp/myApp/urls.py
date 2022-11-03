from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.indexOne, name='indexOne'),
]
# urlpatterns = [
#     path('', views.help, name='help'),
# ]
