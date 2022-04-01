from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.generic import TemplateView

from .views import robots
from .sitemaps import StaticViewSitemap
from courses.sitemaps import courses_sitemap

sitemaps = {
    'static': StaticViewSitemap,
}
sitemaps.update(courses_sitemap)

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('robots.txt', robots, name='robots'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('courses/', include('courses.urls')),
    path('admin/', admin.site.urls),
]
