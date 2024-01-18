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
    salary = models.Geography_salary.objects.all()
    rating = models.Geography_rating.objects.all()
    devops_salary = models.Geography_devops_salary.objects.all()
    devops_rating = models.Geography_devops_rating.objects.all()
    images = models.Geography_charts.objects.all()[0]
    context = {
        "salary": salary,
        "rating": rating,
        "devops_salary": devops_salary,
        "devops_rating": devops_rating,
        "images": images,
    }
    return render(request, "geography_page.html", context=context)


def skills_page(request):
    return HttpResponse('skills')


def recent_vacancies_page(request):
    return HttpResponse('recent')
