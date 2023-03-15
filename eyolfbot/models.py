from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from eyolfbot.discord_client import EyolfbotClient

class User(models.Model):
    discord_id = models.PositiveBigIntegerField(primary_key=True)

    def __str__(self):
        return f'User: {self.discord_id}'

class Role(models.Model):
    discord_id = models.PositiveBigIntegerField(primary_key=True)
    members = models.ManyToManyField(User, through='Membership')

    def __str__(self):
        return f'Role: {self.discord_id}'

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} in {self.role}'

    class Meta:
        unique_together = ('user', 'role')

@receiver(post_save, sender=Membership)
def create_membership(sender, instance, **kwargs):
        client = EyolfbotClient(intents=intents)
        client.run(settings.EYOLFBOT_DISCORD_TOKEN)
