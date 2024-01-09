from django.db import models

class Demand_average_salary(models.Model):
    year = models.IntegerField()
    salary = models.IntegerField()
    chart_image = models.ImageField(upload_to='demand')


class Demand_average_amount(models.Model):
    year = models.IntegerField()
    vacancy_amount = models.IntegerField()
    chart_image = models.ImageField(upload_to='demand')


class Demand_devops_salary(models.Model):
    year = models.IntegerField()
    salary = models.IntegerField()
    chart_image = models.ImageField(upload_to='demand')


class Demand_devops_amount(models.Model):
    year = models.IntegerField()
    vacancy_amount = models.IntegerField()
    chart_image = models.ImageField(upload_to='demand')

