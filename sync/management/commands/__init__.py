from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Synchronizes static files with eyolfson.com'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('sync'))