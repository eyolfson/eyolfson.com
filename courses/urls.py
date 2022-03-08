from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.index, name='index'),
    path('archive/', views.archive, name='archive'),
    path('archive/<slug:institution_slug>/',
         views.archive_institution, name='archive_institution'),
    path('archive/<slug:institution_slug>/<slug:course_slug>/',
         views.archive_course, name='archive_course'),
    path('archive/<slug:institution_slug>/<slug:course_slug>/'
         '<slug:offering_slug>/',
         views.archive_offering, name='archive_offering'),
    path('<slug:course_slug>/', views.course, name='course'),
]
