from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def main_page(request):
    return render(request, "main_page.html")


def demand_page(request):
    avg_salary = models.Demand_average_salary.objects.all()
    avg_amount = models.Demand_average_amount.objects.all()
    devops_salary = models.Demand_devops_salary.objects.all()
    devops_amount = models.Demand_devops_amount.objects.all()
    images = models.Demand_charts.objects.all()[0]
    context = {
        "avg_salary": avg_salary,
        "avg_amount": avg_amount,
        "devops_salary": devops_salary,
        "devops_amount": devops_amount,
        "images": images,
    }
    return render(request, "demand_page.html", context=context)


def geography_page(request):
    return HttpResponse('geography')


def skills_page(request):
    return HttpResponse('skills')


def recent_vacations_page(request):
    return HttpResponse('recent')
