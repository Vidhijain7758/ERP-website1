

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth import authenticate
from datas.forms import CustomUserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import product,select,order
from .forms import LoginForm, select2,OrderForm,ProductForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg, Count, Max, Min, Sum
import datetime
import matplotlib.pyplot as plt
import datetime
from matplotlib.pyplot import figure, title, bar
import numpy as np
import mpld3
from django.views.generic import UpdateView
import matplotlib
from matplotlib import cm


# Create your views here.
def start(request):
    return render(request, 'datas/start.html')


def login1(request):

    myform = LoginForm(request.POST or None)
    if myform.is_valid():

        usern = myform.cleaned_data.get("username")
        passw = myform.cleaned_data.get("password")

        user = authenticate(username=usern, password=passw)
        if user:

                return redirect("/profile")
        else:
            messages.error(request, "Error")



    return render(request, "datas/login.html", {"form": myform})


def login3(request):
    myform = LoginForm(request.POST or None)
    if myform.is_valid():

        usern = myform.cleaned_data.get("username")
        passw = myform.cleaned_data.get("password")

        user = authenticate(username=usern, password=passw)
        if user:

            return redirect("/profile2")
        else:
            messages.error(request, "Error")

    return render(request, "datas/login.html", {"form": myform})

def login2(request):
    myform = LoginForm(request.POST or None)
    if myform.is_valid():

        usern = myform.cleaned_data.get("username")
        passw = myform.cleaned_data.get("password")

        user = authenticate(username=usern, password=passw)
        if user:

            return redirect("/profile1")
        else:
            messages.error(request, "Error")

    return render(request, "datas/login.html", {"form": myform})

def login4(request):
    myform = LoginForm(request.POST or None)
    if myform.is_valid():

        usern = myform.cleaned_data.get("username")
        passw = myform.cleaned_data.get("password")

        user = authenticate(username=usern, password=passw)
        if user:

            return redirect("/profile3")
        else:
            messages.error(request, "Error")

    return render(request, "datas/login.html", {"form": myform})



def select1(request):
    if (request.method == 'POST'):
        form1 = select2(request.POST)
        if (form1.is_valid()):

            a = form1.cleaned_data['sele']

            if(a == 'student'):
                return redirect("/login1")
            elif(a == 'cafeteria'):
                return redirect("/login2")
            elif(a == 'lost_and_found'):
                return redirect("/login3")
            else:
                return redirect("/login4")
        else:
            messages.error(request, "Error")
    else:
        form1 = select2()
        return render(request, 'datas/select.html', {'form': form1})

    args = {'user': request.user}
    return render(request, 'datas/select.html', args)


def register(request):
    if (request.method == 'POST'):
        form = CustomUserCreationForm(request.POST)
        if (form.is_valid()):
            form.save()


            return redirect('/login')
        else:
            messages.error(request, "Error")
    else:
        form = CustomUserCreationForm()

    args = {'form': form}
    return render(request, 'datas/signup.html', args)

def profile2(request):

        products = product.objects.filter(active='1')
        return render(request, 'datas/index_product.html', {'products': products})

def profile3(request):
    args = {'user': request.user}
    return render(request, 'datas/profile3.html', args)


def profile1(request):

    orders = order.objects.all()
    return render(request, 'datas/index.html', {'orders': orders})

def profile(request):
    args = {'user': request.user}
    return render(request,'datas/profile.html',args)

def home(request):

            return render(request,'datas/home.html')
            # return redirect('/result')




def home1(request):
            return render(request,'datas/home1.html')
            # return redirect('/result')

def home2(request):
    return render(request,'datas/home2.html')

def home3(request):
    return render(request,'datas/home3.html')

def check(request):

    return render(request, 'datas/check.html')

def menu(request):

    products = product.objects.filter(active='1')
    return render(request, 'datas/index_product.html', {'products': products})

def order(request):

    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/', messages.success(request, 'Order was successfully created.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = OrderForm()
        return render(request, 'datas/new.html', {'form':form})

def show(request, order_id):
    rder = order.objects.filter(id=order_id)
    return render(request, 'datas/show.html', {'order': order})


def edit(request, order_id):
    rder = order.objects.get(id=order_id)
    if request.POST:
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            if form.save():
                return redirect('/', messages.success(request, 'Order was successfully updated.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = OrderForm(instance = rder)
        return render(request, 'datas/edit.html', {'form':form})

def destroy(request, order_id):
    rder = order.objects.get(id=order_id)
    rder.delete()
    return redirect('/', messages.success(request, 'Order was successfully deleted.', 'alert-success'))

def new_product(request):
    if request.POST:
        form = ProductForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/products', messages.success(request, 'Product was successfully created.', 'alert-success'))
            else:
                return redirect('/products', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/products', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        product_form = ProductForm()
        return render(request, 'datas/new_product.html', {'product_form':product_form})

def destroy_product(request, product_id):


    if product.objects.filter(id=product_id).update(active='0'):
        return redirect('/products', messages.success(request, 'Product was successfully deleted.', 'alert-success'))
    else:
        return redirect('/products', messages.danger(request, 'Cannot delete product while its order exists.', 'alert-danger'))
