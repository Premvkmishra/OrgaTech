from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_event/', views.post_event, name='post_event'),
]