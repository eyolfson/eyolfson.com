from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import (
    Course,
    Institution,
    Link,
    Offering,
    Resource,
)

def get_archive_offerings(**kwargs):
    return Offering.objects.filter(active=False, **kwargs)

def index(request):
    offerings = Offering.objects.filter(active=True)
    return render(request, 'courses/index.html', {
        'offerings': offerings,
        'archive_offerings': get_archive_offerings(),
    })

def offering_detail(request, offering):
    assignments = Resource.assignments.filter(offering=offering)
    lectures = Resource.lectures.filter(offering=offering)
    links = Link.objects.standalone().filter(offering=offering)
    others = Resource.others.filter(offering=offering)
    return render(request, 'courses/offering_detail.html', {
        'assignments': assignments,
        'offering': offering,
        'lectures': lectures,
        'links': links,
        'others': others,
    })

def course(request, course_slug):
    offering = get_object_or_404(Offering,
        course__slug=course_slug,
        active=True,
    )
    return offering_detail(request, offering)

def archive(request):
    return render(request, 'courses/institution_list.html', {
        'offerings': get_archive_offerings(),
    })

def archive_institution(request, institution_slug):
    institution = get_object_or_404(Institution,
        slug=institution_slug,
    )
    if not Offering.objects.filter(course__institution=institution,
                                   active=False).exists():
        raise Http404(f'{institution} has no archived offerings.')
    return render(request, 'courses/course_list.html', {
        'institution': institution,
        'offerings': get_archive_offerings(
            course__institution__slug=institution_slug,
        ),
    })

def archive_course(request, institution_slug, course_slug):
    course = get_object_or_404(Course,
        institution__slug=institution_slug,
        slug=course_slug,
    )
    if not Offering.objects.filter(course=course, active=False).exists():
        raise Http404(f'{course} has no archived offerings.')
    return render(request, 'courses/offering_list.html', {
        'course': course,
        'offerings': get_archive_offerings(
            course__institution__slug=institution_slug,
            course__slug=course_slug,
        ),
    })

def archive_offering(request, institution_slug, course_slug, offering_slug):
    offering = get_object_or_404(Offering,
        course__institution__slug=institution_slug,
        course__slug=course_slug,
        slug=offering_slug,
        active=False,
    )
    return offering_detail(request, offering)

class IndexView(generic.TemplateView):
    template_name = 'courses/index.html'

class InstitutionListView(generic.ListView):
    model = Institution
    template_name = 'courses/institution_list.html'

class OfferingDetailView(generic.DetailView):
    model = Offering
    template_name = 'courses/offering_detail.html'
