from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def drink(request, drink_name):
    drinks = {'mocha': 'type of coffee', 'tea': 'type of beverages', 'lemonade': 'type of refreshment', 'choice_of_drink': drink_name}
    return HttpResponse(f"<h2> {drinks} </h2>")