from django.shortcuts import render

from django.http import JsonResponse
from .models import Contact
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        contact = Contact.objects.create(
            name = data['name'],
            email = data['email'],
            message = data['message']
        )
        return JsonResponse({'message': 'Form submitted successfully.'})
    return JsonResponse({'status': "fail", 'message': "Invalid request method"})