from django.conf import settings
from django.db import models

class Connection(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='eyolfbot_connection',
    )
    utoronto_id = models.CharField(max_length=255, db_index=True)
    discord_id = models.PositiveIntegerField()
    gitlab_id = models.PositiveIntegerField()

    def __str__(self):
        return str(self.user)
