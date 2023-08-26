from django.urls import path

from . import views

app_name = 'eyolfbot'

urlpatterns = [
    path("discord/", views.discord, name='discord'),
]