from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):

    protocol = 'https'

    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)
