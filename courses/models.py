import os

from django.db import models
from django.utils.text import slugify

class Institution(models.Model):

    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Course(models.Model):

    institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE,
    )
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title} ({self.name})'

class Offering(models.Model):

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
    )
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=50)
    start = models.DateField()
    active = models.BooleanField()

    def __str__(self):
        return f'{self.name} {self.course}'

    class Meta:
        ordering = ['-start']

class ResourceQuerySet(models.QuerySet):

    def has_links(self):
        return self.annotate(num_links=models.Count('link')) \
                   .filter(num_links__gt=0).exists()

class ResourceManager(models.Manager):

    def get_queryset(self):
        return ResourceQuerySet(self.model, using=self._db)

class SyllabusManager(ResourceManager):

    def get_queryset(self):
        return super().get_queryset().filter(kind=Resource.Kind.SYLLABUS)

    def has_links(self):
        return self.get_queryset().has_links()

class LectureManager(ResourceManager):

    def get_queryset(self):
        return super().get_queryset().filter(kind=Resource.Kind.LECTURE)

    def has_links(self):
        return self.get_queryset().has_links()

class AssignmentManager(ResourceManager):

    def get_queryset(self):
        return super().get_queryset().filter(kind=Resource.Kind.ASSIGNMENT)

    def has_links(self):
        return self.get_queryset().has_links()

class MidtermManager(ResourceManager):

    def get_queryset(self):
        return super().get_queryset().filter(kind=Resource.Kind.MIDTERM)

    def has_links(self):
        return self.get_queryset().has_links()

class FinalManager(ResourceManager):

    def get_queryset(self):
        return super().get_queryset().filter(kind=Resource.Kind.FINAL)

    def has_links(self):
        return self.get_queryset().has_links()

def resource_path(instance, filename):
    offering = instance.offering
    offering_slug = offering.slug
    course = offering.course
    course_slug = course.slug
    institution = course.institution
    institution_slug = institution.slug
    kind_slug = slugify(Resource.Kind(instance.kind).label)
    if instance.number:
        number = f'-{instance.number}'
    else:
        number = ''
    _, ext = os.path.splitext(filename)
    return f'courses/{institution_slug}/{course_slug}/{offering_slug}/' \
           f'{kind_slug}{number}{ext}'

class Resource(models.Model):

    class Kind(models.IntegerChoices):
        SYLLABUS = 1
        LECTURE = 2
        ASSIGNMENT = 3
        MIDTERM = 4
        FINAL = 5

    offering = models.ForeignKey(
        Offering,
        on_delete=models.CASCADE,
    )
    file = models.FileField(upload_to=resource_path)
    kind = models.IntegerField(choices=Kind.choices)
    title = models.CharField(max_length=50)
    number = models.IntegerField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    due_date_time = models.DateTimeField(blank=True, null=True)

    objects = ResourceQuerySet.as_manager()
    syllabuses = SyllabusManager()
    lectures = LectureManager()
    assignments = AssignmentManager()
    midterms = MidtermManager()
    finals = FinalManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['kind', 'number']

class LinkQuerySet(models.QuerySet):

    def standalone(self):
        return self.filter(resource__isnull=True)

class Link(models.Model):

    offering = models.ForeignKey(
        Offering,
        on_delete=models.CASCADE,
    )
    resource = models.ForeignKey(
        Resource,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    url = models.URLField()
    title = models.CharField(max_length=50)
    number = models.IntegerField(blank=True, null=True)

    objects = LinkQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['number']
