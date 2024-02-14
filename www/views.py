from django.http import HttpResponse
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

def gpg_public_key(request):
    data = b'\x983\x04e\x92F\xd0\x16\t+\x06\x01\x04\x01\xdaG\x0f\x01\x01\x07@I\xe8]\x17x\x14\xaf\xf2\x7fR\x9d\xcd\x97Jt[B~\x1eT\xff\xd5l\xf8g\x0c\xf9/\x1c\x8b\xb8\xd0\xb4$Jonathan Eyolfson <jon@eyolfson.com>\x88\x94\x04\x13\x16\n\x00<\x16!\x04\xf8\xb5!)\xff\x1b)\x9d0\xdd\x91\xd4\x96\xe7g\xa6\xc9\xbaM\x9a\x05\x02e\x92F\xd0\x02\x1b\x01\x05\t\x01\xe2\x85\x00\x04\x0b\t\x08\x07\x05\x15\n\t\x08\x0b\x04\x16\x02\x03\x01\x02\x1e\x05\x02\x17\x80\x00\n\t\x10\x96\xe7g\xa6\xc9\xbaM\x9a\xc4m\x00\xfc\x0c\xac\xf51\xa1\x02z\x00\x00\\\x90\xd0\xc68\xb9\xfd\x9ce!\x9a,\x03j`\xd6\xd5H\xf5`\xea2m\x00\xfe \x05%\xf5!X\xac\xe2\xb5p\xdef\x85\xa4\xea\x08E\xff\xd7P\rJ\xae:\xa1\xd9a8\xe5\x7f\x01\r\xb88\x04e\x92F\xd0\x12\n+\x06\x01\x04\x01\x97U\x01\x05\x01\x01\x07@\xdb\x97\x89\x84\xdc\x9eu\xde\xd8h\x89\xf1}5\x0f\xc4\x8aw;"\\\x9b\x020\x8a\t\x8d\x99\x0c\xa0\xc6P\x03\x01\x08\x07\x88~\x04\x18\x16\n\x00&\x16!\x04\xf8\xb5!)\xff\x1b)\x9d0\xdd\x91\xd4\x96\xe7g\xa6\xc9\xbaM\x9a\x05\x02e\x92F\xd0\x02\x1b\x0c\x05\t\x01\xe2\x85\x00\x00\n\t\x10\x96\xe7g\xa6\xc9\xbaM\x9al\xee\x00\xffV\x7f.\xbf\x85?\x86@\xbeRq\xc8)\xc1]\xbb&G\x84\x86\xa1\xc4a\xc1\xb5\xc6:9L\xe5\xcd\x18\x01\x00\xe7c\xe8r\xb4\x8dd>\xb5V \xd9\xb8$Y\xe7~\xfc\xd70[\x14(\xfd\x12+\xfa\x19\xf1\xe4\xec\t\xb83\x04e\x92F\xd0\x16\t+\x06\x01\x04\x01\xdaG\x0f\x01\x01\x07@\xa6\xb5\xd4f\xdc\x18\x9f\x00n\x95\xcc\xc6\xb8\x04\xa4\xb2{\x0c\xcc3\xe0\x08\xc8\xc3\x18G,\xe3{\xd8t\x88\x88\xf5\x04\x18\x16\n\x00&\x16!\x04\xf8\xb5!)\xff\x1b)\x9d0\xdd\x91\xd4\x96\xe7g\xa6\xc9\xbaM\x9a\x05\x02e\x92F\xd0\x02\x1b\x02\x05\t\x01\xe2\x85\x00\x00\x81\t\x10\x96\xe7g\xa6\xc9\xbaM\x9av \x04\x19\x16\n\x00\x1d\x16!\x04\xf6\xd3\xb7\xab#?\xfb\x02$:\xf6\xd6\xec\x8c\xfd\xe2`\x05\xf6\x97\x05\x02e\x92F\xd0\x00\n\t\x10\xec\x8c\xfd\xe2`\x05\xf6\x97\x16,\x01\x00\xac\'4-\xbc4\xa0\x89\xca\xa6b\xaca\x9f)\x02\xfb\xe9oq\xaf\xb9\xcd\xf5%\\\xe8\xde3\xee\x1c\x87\x00\xffir\xad\xef\xeem\xa6\xcf\x9a\xb1\xa7d_\xfdZ\xdc\xdf\xe9fi\xf9\x99\x86\xe6\x8dm\xa6\xe7L\xdc^\x06 n\x00\xfc\x0c\xd7p\x93\xbcp8\xfcl.I\x7f\xb8\xc9Lw\x03\xcb\xa0R\xdfu\x1b\x04\xeao\x85\xae\x04\x9ap\x81\x01\x00\xa5\x9a\x1b\xd7W\xf33h\x8f\\\xcd\x05\xe5(y\x12\x10)\xe32\xbd\xb1\x05.)A\x88\\w\xcd\xb8\x07\xb83\x04e\x92F\xd0\x16\t+\x06\x01\x04\x01\xdaG\x0f\x01\x01\x07@\xcc\x01\r\xbb`82\\\xc8\x87\xe3\x88[\xd0F\xb4\xae\xa3\x0fh\x0c\x8cE\xffL(]\x97\x028h\xf7\x88~\x04\x18\x16\n\x00&\x16!\x04\xf8\xb5!)\xff\x1b)\x9d0\xdd\x91\xd4\x96\xe7g\xa6\xc9\xbaM\x9a\x05\x02e\x92F\xd0\x02\x1b \x05\t\x01\xe2\x85\x00\x00\n\t\x10\x96\xe7g\xa6\xc9\xbaM\x9a\xa9K\x00\xfd\x1dC\xa2\x9c\xfe\xd2\x97xc\x9b\x01=f\x01\xcbh,\x1b\xe5\xcfr\\\x0c\xfa\x8cz!\xd0\xcb#vi\x00\xff\\\xd2\xd2\xb6\x87\xcd\xabs\xb1\xfcIi\x91]\xce?6\x0f\x19\x19g\xdc\x9b\xd8s\xf6\'c3\xd8t\x03'
    return HttpResponse(data, content_type='application/octet-stream')
