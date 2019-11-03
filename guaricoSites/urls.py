"""guaricoSites URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
#Django
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

#local views
from cities import views as cities_views

urlpatterns = [

    #admin
    path('admin/', admin.site.urls),
    #ciudades
    path('',cities_views.principal_page,name = 'guarico'),
    path('La_Pascua/',cities_views.pascua_page, name = 'pascua'),
    path('tucupido/',cities_views.tucupido_page, name = 'tucupido'),
    path('zaraza/',cities_views.zaraza_page, name = 'zaraza'),
    path('las-mercedes-del-llano/',cities_views.mercedes_page,name = 'mercedes'),
    path('altagracia-de-orituco/',cities_views.altagracia_page,name= 'altagracia'),
    path('San-Juan-de-los-Morros/',cities_views.SanJuan_page,name = 'SanJuan'),
    path('calabozo/',cities_views.calabozo_page,name = 'calabozo'),
    #gastronomia
    path('gastronomia/',TemplateView.as_view(template_name = 'gastronomia.html'),name = 'gastronomia'),
    #festividades
    path('festividades/',TemplateView.as_view(template_name = 'festividades.html'),name = 'festividades'),
    #about
    path('about/',TemplateView.as_view(template_name = 'about.html'),name = 'about'),



] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
