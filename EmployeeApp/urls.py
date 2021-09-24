from django.conf.urls import url
from django.urls.resolvers import URLPattern
from EmployeeApp import views


URLPattern = [
    url(r'^departmment$', views.departmentApi),
    url(r'^departmment/[0-9]+)$'),
]
