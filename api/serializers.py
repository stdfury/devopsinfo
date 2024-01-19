from rest_framework import serializers
from info_pages.models import *


class DemandAverageSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand_average_salary
        fields = ['id', 'year', 'salary']


class DemandAverageAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand_average_amount
        fields = ['id', 'year', 'vacancy_amount']


class DemandDevopsSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand_devops_salary
        fields = ['id', 'year', 'salary']


class DemandDevopsAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand_devops_amount
        fields = ['id', 'year', 'vacancy_amount']


class DemandChartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand_charts
        fields = ['id', 'average_salary', 'average_amount', 'devops_salary', 'devops_amount']


class GeographySalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Geography_salary
        fields = ['id', 'city', 'salary']


class GeographyRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geography_rating
        fields = ['id', 'city', 'rate']


class GeographyDevopsSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Geography_devops_salary
        fields = ['id', 'city', 'salary']


class GeographyDevopsRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geography_devops_rating
        fields = ['id', 'city', 'rate']


class GeographyChartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geography_charts
        fields = ['id', 'salary', 'rating', 'devops_salary', 'devops_rating']
