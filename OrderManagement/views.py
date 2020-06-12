from django.shortcuts import render
from django.http import HttpResponse
from OrderManagement.models import Articles

# Create your views here.


def search_products(request):
    return render(request, "search_products.html")


def search(request):
    if request.GET["prod"]:
        # message = "Searched article: {}".format(request.GET["prod"])
        product = request.GET["prod"]
        articles = Articles.objects.filter(name__icontains=product)
        # message = "Found {}. Price = {}".format(articles.name, articles.price)
        return render(request, "search_results.html", {"articles":articles, "query":product})
    else:
        message = "Search filed was empty!"
    return HttpResponse(message)
