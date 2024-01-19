from rest_framework import generics
from .serializers import *


class DemandAverageSalaryListCreate(generics.ListCreateAPIView):
    queryset = Demand_average_salary.objects.all()
    serializer_class = DemandAverageSalarySerializer


class DemandAverageAmountListCreate(generics.ListCreateAPIView):
    queryset = Demand_average_amount.objects.all()
    serializer_class = DemandAverageAmountSerializer


class DemandDevopsSalaryListCreate(generics.ListCreateAPIView):
    queryset = Demand_devops_salary.objects.all()
    serializer_class = DemandDevopsSalarySerializer


class DemandDevopsAmountListCreate(generics.ListCreateAPIView):
    queryset = Demand_devops_amount.objects.all()
    serializer_class = DemandDevopsAmountSerializer


class GeographySalaryListCreate(generics.ListCreateAPIView):
    queryset = Geography_salary.objects.all()
    serializer_class = GeographySalarySerializer


class GeographyRatingListCreate(generics.ListCreateAPIView):
    queryset = Geography_rating.objects.all()
    serializer_class = GeographyRatingSerializer


class GeographyDevopsSalaryListCreate(generics.ListCreateAPIView):
    queryset = Geography_devops_salary.objects.all()
    serializer_class = GeographyDevopsSalarySerializer


class GeographyDevopsRatingListCreate(generics.ListCreateAPIView):
    queryset = Geography_devops_rating.objects.all()
    serializer_class = GeographyDevopsRatingSerializer


class DemandChartsListCreate(generics.ListCreateAPIView):
    queryset = Demand_charts.objects.all()
    serializer_class = DemandChartsSerializer


class GeographyChartsListCreate(generics.ListCreateAPIView):
    queryset = Geography_charts.objects.all()
    serializer_class = GeographyChartsSerializer
