from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def machine_learning(request):
    return render (request, 'machine_learning/machine_learning.html')

def random(request):
    return render (request, 'machine_learning/random_forest.html')


def k_nearest(request):
    return render (request, 'machine_learning/knn.html')


def dtree(request):
    return render (request, 'machine_learning/DT.html')

