from django.shortcuts import render
from django.http import JsonResponse
from Apache_api.models import apache

# Create your views here.
def Apache_list(request):
    Apache = Apache.objects.all() #Complex Data
    Apache_Python = list(Apache.values()) #Python DS
    return JsonResponse({
        'Apache': Apache_Python
    })