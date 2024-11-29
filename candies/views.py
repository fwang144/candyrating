from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Candy

def candies(request):
    mycandies = Candy.objects.all().values()
    template = loader.get_template('candy.html')
    context = {
        "mycandies": mycandies,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mycandy = Candy.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
    'mycandy': mycandy,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
    