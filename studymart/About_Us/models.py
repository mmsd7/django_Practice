from django.http import HttpResponse
from django.db import models

# Create your models here.
def about_us(request):
    return HttpResponse('This is about us section.')
