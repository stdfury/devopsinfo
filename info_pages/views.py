from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main_page(request):
    return render(request, "main_page.html")


def demand_page(request):
    return HttpResponse('demand')


def geography_page(request):
    return HttpResponse('geography')


def skills_page(request):
    return HttpResponse('skills')


def recent_vacations_page(request):
    return HttpResponse('recent')
