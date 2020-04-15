"""geodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
# from django.contrib import admin

from django.contrib.gis import admin
from django.urls import include, path

from transformer_model.views import search_by_peano, count_by_flag, \
                                    map_request, index, map_query_extend, \
                                    dashboard, update_attribute_transformer

from aoj_model.views import select_aoj_request

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^admin/', admin.site.urls),
    url(r'^search/', search_by_peano),
    url(r'^count/', count_by_flag),
    url(r'^show/', map_request),
    url(r'^index/', index),
    url(r'^home/', dashboard),
    url(r'^query/', map_query_extend),
    url(r'^update/', update_attribute_transformer),
    url(r'^aoj_select/', select_aoj_request),
    
    ]
