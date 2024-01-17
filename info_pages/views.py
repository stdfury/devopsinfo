from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def main_page(request):
    return render(request, "main_page.html")


def demand_page(request):
    data = models.Demand_average_salary.objects.all()
    images = models.Demand_charts.objects.get(id=1)
    context = {
        "data": data,
        "images": images,
    }
    return render(request, "demand_page.html", context=context)


def geography_page(request):
    return HttpResponse('geography')


def skills_page(request):
    return HttpResponse('skills')


def recent_vacations_page(request):
    return HttpResponse('recent')
