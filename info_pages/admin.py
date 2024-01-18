from django.contrib import admin
from . import models

admin.site.register(models.Demand_devops_amount)
admin.site.register(models.Demand_devops_salary)
admin.site.register(models.Demand_average_amount)
admin.site.register(models.Demand_average_salary)
admin.site.register(models.Demand_charts)

admin.site.register(models.Geography_rating)
admin.site.register(models.Geography_devops_salary)
admin.site.register(models.Geography_devops_rating)
admin.site.register(models.Geography_salary)
admin.site.register(models.Geography_charts)