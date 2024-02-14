from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from rest_framework import routers

from .views import IndexView, gpg_policy_file, gpg_public_key, robots
from .sitemaps import StaticViewSitemap
from courses.sitemaps import courses_sitemap

from eyolfbot.views import discord, ConnectionViewSet

sitemaps = {
    'static': StaticViewSitemap,
}
sitemaps.update(courses_sitemap)

router = routers.DefaultRouter()
router.register(r'eyolfbot/connection', ConnectionViewSet)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view()),
    path('', include('eyolfbot.urls', namespace='eyolfbot')),
    path('social/', include('social_django.urls', namespace='social')),
    path('robots.txt', robots, name='robots'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('courses/', include('courses.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('.well-known/openpgpkey/policy', gpg_policy_file),
    path('.well-known/openpgpkey/hu/euh8tm9f856gpp58qk6aezismfnq5yt1', gpg_public_key),
]
