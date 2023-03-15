from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from .views import IndexView, robots
from .sitemaps import StaticViewSitemap
from courses.sitemaps import courses_sitemap

sitemaps = {
    'static': StaticViewSitemap,
}
sitemaps.update(courses_sitemap)

from rest_framework import routers
from eyolfbot.views import UserViewSet, RoleViewSet, MembershipViewSet
router = routers.DefaultRouter()
router.register(r'eyolfbot/users', UserViewSet)
router.register(r'eyolfbot/roles', RoleViewSet)
router.register(r'eyolfbot/memberships', MembershipViewSet)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('robots.txt', robots, name='robots'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('courses/', include('courses.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
