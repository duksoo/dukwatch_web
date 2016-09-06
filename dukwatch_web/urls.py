"""dukwatch_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from dukwatch.views import swagger_view,sample_page,sample_api

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest-api/', include('rest_framework.urls')),
    url(r'^rest-swagger/', swagger_view),
    url(r'^sample_page/', sample_page),
    url(r'^api/sample/', sample_api.as_view())
]
