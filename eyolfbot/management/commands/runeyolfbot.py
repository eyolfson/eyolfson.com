from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from eyolfbot.discord_client import EyolfbotClient

class Command(BaseCommand):

    help = 'Runs the Eyolfbot Discord client'

    def handle(self, *args, **options):
        if settings.EYOLFBOT_DISCORD_TOKEN == '':
            raise CommandError('EYOLFBOT_DISCORD_TOKEN not set')

        intents = discord.Intents.default()
        intents.members = True

        client = EyolfbotClient(intents=intents)
        client.run(settings.EYOLFBOT_DISCORD_TOKEN)
