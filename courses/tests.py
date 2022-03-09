from datetime import date
from django.db import IntegrityError
from django.test import TestCase
from .models import (
    Course,
    Institution,
    Link,
    Offering,
    Resource,
)

class CoursesTestCase(TestCase):

    def setUp(self):
        institution = Institution.objects.create(
            slug='institution-slug',
            name='Institution Name',
        )
        course = Course.objects.create(
            institution=institution,
            slug='course-slug',
            name='Course Name',
            title='Course Title',
        )
        offering = Offering.objects.create(
            course=course,
            slug='offering-slug',
            name='Offering Name',
            start=date(2021, 3, 9),
            active=True,
        )
        lecture_resource = Resource.objects.create(
            offering=offering,
            kind=Resource.Kind.LECTURE,
            number=1,
            title='Lecture 1 Title',
        )
        syllabus_resource = Resource.objects.create(
            offering=offering,
            kind=Resource.Kind.SYLLABUS,
            number=None,
            title='Syllabus Title',
        )
        offering_link = Link.objects.create(
            offering=offering,
            number=1,
            title='Offering Link',
        )
        lecture_resource_link = Link.objects.create(
            resource=lecture_resource,
            number=1,
            title='Lecture 1 Link',
        )

    def test_resource_unique_number(self):
        offering = Offering.objects.get(slug='offering-slug')
        with self.assertRaises(IntegrityError):
            Resource.objects.create(
                offering=offering,
                kind=Resource.Kind.LECTURE,
                number=1,
                title='Lecture 1 Title',
            )

    def test_resource_unique_kind_null_number(self):
        offering = Offering.objects.get(slug='offering-slug')
        with self.assertRaises(IntegrityError):
            Resource.objects.create(
                offering=offering,
                kind=Resource.Kind.SYLLABUS,
                number=None,
                title='Syllabus Title',
            )

    def test_link_not_both_offering_and_resource(self):
        offering = Offering.objects.get(slug='offering-slug')
        resource = Resource.objects.get(
            offering=offering,
            kind=Resource.Kind.LECTURE,
            number=1,
        )
        with self.assertRaises(IntegrityError):
            Link.objects.create(
                offering=offering,
                resource=resource,
            )

    def test_link_not_null_offering_and_resource(self):
        with self.assertRaises(IntegrityError):
            Link.objects.create()

    def test_offering_link_unique_number(self):
        offering = Offering.objects.get(slug='offering-slug')
        with self.assertRaises(IntegrityError):
            Link.objects.create(offering=offering, number=1)

    def test_offering_link_many_null_number(self):
        offering = Offering.objects.get(slug='offering-slug')
        l1 = Link.objects.create(
            offering=offering,
            number=None,
            title='Link 1',
        )
        l2 = Link.objects.create(
            offering=offering,
            number=None,
            title='Link 2',
        )
        l1.delete()
        l2.delete()

    def test_resource_link_unique_number(self):
        offering = Offering.objects.get(slug='offering-slug')
        resource = Resource.objects.get(
            offering=offering,
            kind=Resource.Kind.LECTURE,
            number=1,
        )
        with self.assertRaises(IntegrityError):
            Link.objects.create(resource=resource, number=1)

    def test_resource_link_many_null_number(self):
        offering = Offering.objects.get(slug='offering-slug')
        resource = Resource.objects.get(
            offering=offering,
            kind=Resource.Kind.LECTURE,
            number=1,
        )
        l1 = Link.objects.create(
            resource=resource,
            number=None,
            title='Link 1',
        )
        l2 = Link.objects.create(
            resource=resource,
            number=None,
            title='Link 2',
        )
        l1.delete()
        l2.delete()
