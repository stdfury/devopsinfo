from django.db import models

class Demand_average_salary(models.Model):
    year = models.IntegerField()
    salary = models.IntegerField()


class Demand_average_amount(models.Model):
    year = models.IntegerField()
    vacancy_amount = models.IntegerField()


class Demand_devops_salary(models.Model):
    year = models.IntegerField()
    salary = models.IntegerField()


class Demand_devops_amount(models.Model):
    year = models.IntegerField()
    vacancy_amount = models.IntegerField()

class Demand_charts(models.Model):
    average_salary = models.ImageField(upload_to='demand')
    average_amount = models.ImageField(upload_to='demand')
    devops_salary = models.ImageField(upload_to='demand')
    devops_amount = models.ImageField(upload_to='demand')
