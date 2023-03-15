from django.contrib import admin
from .models import (
    User,
    Role,
    Membership,
)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    pass
