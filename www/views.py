from django.urls import reverse
from django.views.generic import TemplateView

class RobotsView(TemplateView):

    template_name="robots.txt"
    content_type="text/plain"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sitemap'] = self.request.build_absolute_uri(
            reverse('django.contrib.sitemaps.views.sitemap')
        )
        return context