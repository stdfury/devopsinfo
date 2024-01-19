from django.urls import path
from . import views

urlpatterns = [
    path('demand/average-salary/', views.DemandAverageSalaryListCreate.as_view()),
    path('demand/average-salary/<int:year>/', views.DemandAverageSalaryListCreate.as_view()),
    path('demand/average-amount/', views.DemandAverageAmountListCreate.as_view()),
    path('demand/average-amount/<int:year>/', views.DemandAverageAmountListCreate.as_view()),
    path('demand/devops-salary/', views.DemandDevopsSalaryListCreate.as_view()),
    path('demand/devops-salary/<int:year>/', views.DemandDevopsSalaryListCreate.as_view()),
    path('demand/devops-amount/', views.DemandDevopsAmountListCreate.as_view()),
    path('demand/devops-amount/<int:year>/', views.DemandDevopsAmountListCreate.as_view()),
    path('demand/charts/', views.DemandChartsListCreate.as_view()),

    path('geography/salary/', views.GeographySalaryListCreate.as_view()),
    path('geography/salary/<str:city>/', views.GeographySalaryListCreate.as_view()),
    path('geography/rating/', views.GeographyRatingListCreate.as_view()),
    path('geography/rating/<str:city>/', views.GeographyRatingListCreate.as_view()),
    path('geography/devops-salary/', views.GeographyDevopsSalaryListCreate.as_view()),
    path('geography/devops-salary/<str:city>/', views.GeographyDevopsSalaryListCreate.as_view()),
    path('geography/devops-rating/', views.GeographyDevopsRatingListCreate.as_view()),
    path('geography/devops-rating/<str:city>/', views.GeographyDevopsRatingListCreate.as_view()),
    path('geography/charts/', views.GeographyChartsListCreate.as_view()),
]
