from django.db import models
from django.shortcuts import redirect, render
from .models import Dojos, Ninjas

def index(request):
    context = {
        'dojos' : Dojos.objects.all(),
        'ninjas' : Ninjas.objects.all(),
    }
    return render(request, "home.html", context)
    

def add_dojo(request):
    name = request.POST['name']       
    city = request.POST['city']
    state = request.POST['state']
    desc = request.POST['desc']
    # ninjas = list of ninjas
    Dojos.objects.create (name = name, city = city, state = state, descr = desc)
    return redirect('/')

def add_ninja(request):
    this_dojo = Dojos.objects.get(id=request.POST['dojo_id'])
    first_name = request.POST['first_name']       
    last_name = request.POST['last_name']
    dojo = this_dojo
    Ninjas.objects.create (first_name = first_name, last_name = last_name, dojo = dojo)
    return redirect('/')
