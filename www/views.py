from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.generic import TemplateView

from courses.models import Offering

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['active_offerings'] = Offering.objects.filter(active=True)
        return context

def robots(request):
    sitemap = request.build_absolute_uri(
        reverse("django.contrib.sitemaps.views.sitemap")
    )
    return TemplateResponse(
        request,
        "robots.txt",
        {"sitemap": sitemap},
        content_type="text/plain",
    )
