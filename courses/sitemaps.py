from django.conf import settings
from django.contrib import sitemaps
from django.urls import reverse

from .models import Course, Institution, Offering, Resource

class StaticViewSitemap(sitemaps.Sitemap):

    changefreq = 'monthly'
    protocol = 'https'

    def items(self):
        return ['courses:index', 'courses:archive']

    def location(self, item):
        return reverse(item)

class CourseSitemap(sitemaps.Sitemap):

    changefreq = 'monthly'
    protocol = 'https'

    def items(self):
        return Course.objects.with_archived_offerings()

class InstitutionSitemap(sitemaps.Sitemap):

    changefreq = 'monthly'
    protocol = 'https'

    def items(self):
        return Institution.objects.with_archived_offerings()

class InactiveOfferingSitemap(sitemaps.Sitemap):

    changefreq = 'never'
    protocol = 'https'

    def items(self):
        return Offering.objects.filter(active=False)

class ActiveOfferingSitemap(sitemaps.Sitemap):

    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return Offering.objects.filter(active=True)

courses_sitemap = {
    'courses_static': StaticViewSitemap,
    'courses_institution': InstitutionSitemap,
    'courses_course': CourseSitemap,
    'courses_inactive_offering': InactiveOfferingSitemap,
    'courses_active_offering': ActiveOfferingSitemap,
}
