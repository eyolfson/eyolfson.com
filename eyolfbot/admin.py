from django.contrib import admin

from .models import Connection

@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    pass
