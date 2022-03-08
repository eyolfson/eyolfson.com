from django.contrib import admin

from .models import (
    Course,
    Institution,
    Link,
    Offering,
    Resource,
)

admin.site.register(Course)
admin.site.register(Institution)
admin.site.register(Link)
admin.site.register(Offering)
admin.site.register(Resource)
