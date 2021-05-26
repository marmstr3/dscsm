from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Project


# General Methods
def paginate(request, list_objects, items_per_page):
    paginator = Paginator(list_objects, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return page_obj


# Views
def project_list(request):
    projects = Project.objects.filter(last_edited_date__lte=timezone.now()).order_by('-last_edited_date')
    page_obj = paginate(request, projects, 4)

    return render(request,
                  '../templates/projects_list.html',
                  {'page_name': "Portfolio",
                  'page_obj': page_obj,
                   }
                  )