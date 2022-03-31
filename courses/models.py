import os

from django.db import models
from django.urls import reverse, NoReverseMatch
from django.utils.text import slugify

class InstitutionQuerySet(models.QuerySet):

    def with_archived_offerings(self):
        return self.annotate(
            num_archived_offerings=models.Count(
                'course__offering',
                filter=models.Q(course__offering__active=False)
            )
        ).filter(num_archived_offerings__gt=0)

class Institution(models.Model):

    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=50)

    objects = InstitutionQuerySet.as_manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if Offering.objects.filter(course__institution=self,
                                   active=False) \
                           .exists():
            return reverse('courses:archive_institution',
                            kwargs={'institution_slug': self.slug})
        raise NoReverseMatch(f'{self} has no archived offerings')

    class Meta:
        ordering = ['name']

class CourseQuerySet(models.QuerySet):

    def with_archived_offerings(self):
        return self.annotate(
            num_archived_offerings=models.Count(
                'offering', filter=models.Q(offering__active=False)
            )
        ).filter(num_archived_offerings__gt=0)

class Course(models.Model):

    institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE,
    )
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=80)

    objects = CourseQuerySet.as_manager()

    def __str__(self):
        return f'{self.title} ({self.name})'

    def get_absolute_url(self):
        if Offering.objects.filter(course=self, active=False).exists():
            return reverse('courses:archive_course', kwargs={
                'institution_slug': self.institution.slug,
                'course_slug': self.slug,
            })
        raise NoReverseMatch(f'{self} has no archived offerings')

    class Meta:
        ordering = ['title']

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

    def get_absolute_url(self):
        if self.active:
            return reverse('courses:course', kwargs={'course_slug': self.course.slug})
        else:
            return reverse('courses:archive_offering', kwargs={
                'institution_slug': self.course.institution.slug,
                'course_slug': self.course.slug,
                'offering_slug': self.slug,
            })

    class Meta:
        ordering = ['-start', 'name']

class ResourceQuerySet(models.QuerySet):

    def has_links(self):
        return self.annotate(num_links=models.Count('link')) \
                   .filter(num_links__gt=0).exists()

    def has_numbers(self):
        return self.filter(number__isnull=False).exists()

class ResourceManager(models.Manager):

    def get_queryset(self):
        return ResourceQuerySet(self.model, using=self._db)

class LectureManager(ResourceManager):

    def get_queryset(self):
        return super().get_queryset().filter(kind=Resource.Kind.LECTURE)

    def has_links(self):
        return self.get_queryset().has_links()

    def has_numbers(self):
        return self.get_queryset().has_numbers()

class AssignmentManager(ResourceManager):

    def get_queryset(self):
        return super().get_queryset().filter(kind=Resource.Kind.ASSIGNMENT)

    def has_links(self):
        return self.get_queryset().has_links()

    def has_numbers(self):
        return self.get_queryset().has_numbers()

class OtherManager(ResourceManager):

    def get_queryset(self):
        return super().get_queryset().filter(
            models.Q(kind=Resource.Kind.SYLLABUS)
            | models.Q(kind=Resource.Kind.MIDTERM)
            | models.Q(kind=Resource.Kind.FINAL)
        )

    def has_links(self):
        return self.get_queryset().has_links()

    def has_numbers(self):
        return self.get_queryset().has_numbers()

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
    title = models.CharField(max_length=80)
    number = models.IntegerField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    due_date_time = models.DateTimeField(blank=True, null=True)

    objects = ResourceQuerySet.as_manager()
    lectures = LectureManager()
    assignments = AssignmentManager()
    others = OtherManager()

    def __str__(self):
        kind_label = Resource.Kind(self.kind).label
        if self.number is not None:
            number = f' {self.number}'
        else:
            number = ''
        return f'{self.title} - {kind_label}{number} - {self.offering}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['offering', 'kind'],
                name='unique_offering_and_kind_with_null_number',
                condition=models.Q(number__isnull=True),
            ),
        ]
        ordering = ['offering', 'kind', 'number', 'title']
        unique_together = ['offering', 'kind', 'number']

class LinkQuerySet(models.QuerySet):

    def standalone(self):
        return self.filter(resource__isnull=True)

class Link(models.Model):

    offering = models.ForeignKey(
        Offering,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    resource = models.ForeignKey(
        Resource,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    url = models.URLField()
    title = models.CharField(max_length=80)
    number = models.IntegerField(blank=True, null=True)

    objects = LinkQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(offering__isnull=True, resource__isnull=False)
                      | models.Q(offering__isnull=False, resource__isnull=True),
                name='mutually_exclusive_offering_or_resource'),
        ]
        ordering = ['offering', 'resource', 'number', 'title']
        unique_together = [
            ['offering', 'number'],
            ['resource', 'number'],
        ]
