import os
import urllib.request

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

STATICFILES_PATHS = [
    'cv.pdf',
    'css/main.css',
    'images/headshot.jpg',
    'images/icon-128.png',
]

class Command(BaseCommand):
    help = 'Synchronize static files with eyolfson.com'

    def handle(self, *args, **options):
        staticfiles_dir = settings.STATICFILES_DIRS[0]
        if len(settings.STATICFILES_DIRS) > 1:
            self.stdout.write(self.style.WARNING(
                f'Using staticfile dir: {staticfiles_dir}'
            ))

        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]

        for path in STATICFILES_PATHS:
            full_path = os.path.join(staticfiles_dir, path)
            if os.path.exists(full_path):
                continue
            url = f'https://eyolfson.com/static/{path}'
            with opener.open(url) as input, open(full_path, 'wb') as output:
                while True:
                    data = input.read(4096)
                    if data:
                        output.write(data)
                    else:
                        break
            self.stdout.write(self.style.SUCCESS(f'Downloaded: {path}'))
