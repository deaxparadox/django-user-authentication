from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def error_404(request):
    return HttpResponse("<h2>Page not found :(</h2>")