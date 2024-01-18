from django.db import models

# Модели для страницы "Востребованность"

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


# Модели для страницы "География"
class Geography_salary(models.Model):
    city = models.CharField()
    salary = models.IntegerField()


class Geography_rating(models.Model):
    city = models.CharField()
    rate = models.FloatField()


class Geography_devops_salary(models.Model):
    city = models.CharField()
    salary = models.IntegerField()


class Geography_devops_rating(models.Model):
    city = models.CharField()
    rate = models.FloatField()


class Geography_charts(models.Model):
    salary = models.ImageField(upload_to='demand')
    rating = models.ImageField(upload_to='demand')
    devops_salary = models.ImageField(upload_to='demand')
    devops_rating = models.ImageField(upload_to='demand')