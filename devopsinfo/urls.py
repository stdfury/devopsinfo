"""
URL configuration for devopsinfo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from info_pages import views as v

urlpatterns = [
    path('', v.main_page, name="main"),
    path('api/', include('api.urls')),
    path('demand/', v.demand_page, name="demand"),
    path('geography/', v.geography_page, name="geography"),
    path('skills/', v.skills_page, name="skills"),
    path('recent_vacancies/', v.recent_vacancies_page, name="recent_vacancies"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
