"""postgis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from djangopostgis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('country_states', views.country_states, name='country_states'),
    path('map_name', views.map_name),
    path('map2_name', views.map2_name),
    path('upload_shapefile', views.upload_shapefile),
    path('show_onmap', views.show_onmap) ,
    path('readfile', views.readfile),
    path('india_district', views.india_district, name ='india_district'),   
    # path('csv_to_geojson', views.csv_to_geojson, name ='csv_to_geojson'),
    path('uploadshp', views.uploadshp, name ='uploadshp'), 
    #####csv data######
    path('upload_csv', views.upload_csv, name ='upload_csv'), 
    path('readfile2', views.readfile2, name ='readfile2'), 
    # path('service', views.service, name ='service'),  
    path('data_view_onmap2', views.data_view_onmap2, name ='data_view_onmap2'), 
]  

