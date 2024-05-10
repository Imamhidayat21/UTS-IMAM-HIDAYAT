
from django.contrib import admin
from django.urls import path
from Apache_api.views import Apache_list

urlpatterns = [
    path('list/', Apache_list)
]


