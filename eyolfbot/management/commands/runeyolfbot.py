from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

import discord

class EyolfbotClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.role_message_id = 1018635043117211760
        self.emoji_to_role = {
            discord.PartialEmoji(name='1️⃣'): 1018618993206112316,
            discord.PartialEmoji(name='2️⃣'): 1018619160021966990,
            discord.PartialEmoji(name='3️⃣'): 1018619236232462506,
        }

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_raw_reaction_add(self,
                                  payload: discord.RawReactionActionEvent):
        # Make sure that the message the user is reacting to is the one we care
        # about
        if payload.message_id != self.role_message_id:
            return

        # Check if we're still in the guild and it's cached
        guild = self.get_guild(payload.guild_id)
        if guild is None:
            return

        # If the emoji isn't the one we care about then exit as well
        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            return

        # Make sure the role still exists and is valid
        role = guild.get_role(role_id)
        if role is None:
            return

        # Finally, add the role
        try:
            await payload.member.add_roles(role)
        except discord.HTTPException as e:
            pass

    async def on_raw_reaction_remove(self,
                                     payload: discord.RawReactionActionEvent):
        # Make sure that the message the user is reacting to is the one we care
        # about
        if payload.message_id != self.role_message_id:
            return

        # Check if we're still in the guild and it's cached
        guild = self.get_guild(payload.guild_id)
        if guild is None:
            return

        # Check that the emoji maps to a role
        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            return

        # Get that role on the server (guild)
        role = guild.get_role(role_id)
        if role is None:
            return

        # The payload for `on_raw_reaction_remove` does not provide `.member`
        # so we must get the member ourselves from the payload's `.user_id`
        member = guild.get_member(payload.user_id)
        if member is None:
            # Make sure the member still exists and is valid.
            return

        # Finally, remove the role
        try:
            await member.remove_roles(role)
        except discord.HTTPException as e:
            pass

class Command(BaseCommand):

    help = 'Runs the Eyolfbot Discord client'

    def handle(self, *args, **options):
        if settings.EYOLFBOT_DISCORD_TOKEN == '':
            raise CommandError('EYOLFBOT_DISCORD_TOKEN not set')

        intents = discord.Intents.default()
        intents.members = True

        client = EyolfbotClient(intents=intents)
        client.run(settings.EYOLFBOT_DISCORD_TOKEN)
