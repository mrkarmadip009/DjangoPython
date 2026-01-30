# LAB_1/LAB_1/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, LAB_1 Home!")
