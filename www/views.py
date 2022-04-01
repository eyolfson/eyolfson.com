from django.template.response import TemplateResponse
from django.urls import reverse

def robots(request):
    sitemap = request.build_absolute_uri(
        reverse("django.contrib.sitemaps.views.sitemap")
    )
    return TemplateResponse(
        request,
        'robots.txt',
        {"sitemap": sitemap},
        content_type='text/plain',
    )
