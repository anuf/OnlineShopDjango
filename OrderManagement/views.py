from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def search_products(request):
    return render(request, "search_products.html")


def search(request):
    message = "Searched article: {}".format(request.GET["prod"])
    return HttpResponse(message)
