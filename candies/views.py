from django.shortcuts import render, redirect
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

def addcandy(request):
    namecandy = request.POST["name"]
    typecandy = request.POST["candytype"]
    ratingcandy = request.POST['rating']
    Candy.objects.create(name = namecandy, type = typecandy, rating = ratingcandy)
    return redirect("/")

def editcandy(request, id):
    mycandy = Candy.objects.get(id=id)
    template = loader.get_template('edit.html')
    context = {
        "mycandy": mycandy,
    }

    return HttpResponse(template.render(context, request))

def editcandyprocess(request, id):
    oldcandy = Candy.objects.get(id=id)
    oldcandy.name = request.POST["name"]
    oldcandy.type = request.POST["candytype"]
    oldcandy.rating = request.POST["rating"]
    oldcandy.save()
    return redirect('/')

def delete(request, id):
    mycandy = Candy.objects.get(id=id)
    mycandy.delete()
    return redirect('/')

     
    