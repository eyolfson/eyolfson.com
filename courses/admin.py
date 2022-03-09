from django.contrib import admin
from .models import (
    Course,
    Institution,
    Link,
    Offering,
    Resource,
)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    pass

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource', 'offering')

@admin.register(Offering)
class OfferingAdmin(admin.ModelAdmin):
    pass

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'kind', 'number', 'offering')
