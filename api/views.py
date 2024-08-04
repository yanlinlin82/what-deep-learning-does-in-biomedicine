from django.shortcuts import render
from django.http import JsonResponse

def api_endpoint(request):
    return JsonResponse({'message': 'Hello, World!'})
