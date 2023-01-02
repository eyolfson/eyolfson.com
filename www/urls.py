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

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('robots.txt', robots, name='robots'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('courses/', include('courses.urls')),
    path('admin/', admin.site.urls),
]
