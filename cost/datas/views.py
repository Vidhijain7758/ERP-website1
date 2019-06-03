from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth import authenticate
from datas.forms import CustomUserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import cost,minu,expenses
from .forms import LoginForm, ABC1,ABC2,query2,query
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg, Count, Max, Min, Sum
from .forms import query
import datetime


# Create your views here.
def loginpage(request):
    myform = LoginForm(request.POST or None)
    if myform.is_valid():
        status = request.User.last_name
        usern = myform.cleaned_data.get("username")
        passw = myform.cleaned_data.get("password")

        user = authenticate(username=usern, password=passw)
        if user:
            return redirect("/profile1")
        else:
            messages.error(request, "Error")



    return render(request, "datas/login.html", {"form": myform})


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


def profile1(request):
    if (request.method == 'POST'):
        form = ABC1(request.POST)
        if (form.is_valid()):

            obj = cost()
            obj.line = form.cleaned_data['line_no']
            obj.month = form.cleaned_data['month']
            obj.year = form.cleaned_data['year']
            obj.factoryname =form.cleaned_data['factoryname']
            obj.item_no = form.cleaned_data['item_no']
            obj.section=form.cleaned_data['section']
            obj.department = form.cleaned_data['department']
            obj.category = form.cleaned_data['category']
            obj.style_name=form.cleaned_data['style_name']
            obj.style_number = form.cleaned_data['style_no']
            obj.sub_category = form.cleaned_data['sub_category']
            m = form.cleaned_data['line_no']
            factoryname =form.cleaned_data['factoryname']
            month = form.cleaned_data['month']
            year = form.cleaned_data['year']
            g = cost.objects.all().filter(factoryname=factoryname)
            c = helper_func(month,year)
            a = form.cleaned_data['manpower']
            b = int(form.cleaned_data['operator'])

            total =expenses.objects.all().filter(factoryname = factoryname).values('total')

            y =0
            for i in total:
                y = i


            sum = b+ int(y)
            try:
                e = sum/(a*c)
            except ZeroDivisionError:
                e = 0

            if (m == 'EP_1'):
                obj.EP_1_manpower = a
                obj.EP_1_operator = b
                obj.EP_1_minutes = c
                obj.EP_1_cost = e

            elif (m == 'EP_2'):
                obj.EP_2_manpower = a
                obj.EP_2_operator = b
                obj.EP_2_minutes = c
                obj.EP_2_cost = e
            elif (m == 'EP_3'):
                obj.EP_3_manpower = a
                obj.EP_3_operator = b
                obj.EP_3_minutes = c
                obj.EP_3_cost = e
            elif (m == 'EP_4'):
                obj.EP_4_manpower = a
                obj.EP_4_operator = b
                obj.EP_4_minutes = c
                obj.EP_4_cost = e
            elif (m == 'EP_5'):
                obj.EP_5_manpower = a
                obj.EP_5_operator = b
                obj.EP_5_minutes = c
                obj.EP_5_cost = e
            elif (m == 'EP_6'):
                obj.EP_6_manpower = a
                obj.EP_6_operator = b
                obj.EP_6_minutes = c
                obj.EP_6_cost = e
            elif (m == 'EP_7'):
                obj.EP_7_manpower = a
                obj.EP_7_operator = b
                obj.EP_7_minutes = c
                obj.EP_7_cost = e
            elif (m == 'EP_8'):
                obj.EP_8_manpower = a
                obj.EP_8_operator = b
                obj.EP_8_minutes = c
                obj.EP_8_cost = e
            elif (m == 'EP_9'):
                obj.EP_9_manpower = a
                obj.EP_9_operator = b
                obj.EP_9_minutes = c
                obj.EP_9_cost = e
            elif (m == 'EP_10'):
                obj.EP_10_manpower = a
                obj.EP_10_operator = b
                obj.EP_10_minutes = c
                obj.EP_10_cost = e



            t = str(obj.month)
            d = str(obj.year)
            c = 0
            for i in g:
                if (str(i.day) == t and str(i.year) == d):
                    c = c + 1
            if (c == 0):
                obj.save()
                return redirect('/profile1/check')
            else:
                c = 0
                return redirect('/profile1')


        else:
            messages.error(request, "Error")
    else:
        form = ABC1()
        return render(request, 'datas/profile.html', {'form': form})

    args = {'user': request.user}
    return render(request, 'datas/profile.html', args)


def profile2(request):
    if (request.method == 'POST'):
        form = ABC2(request.POST)
        if (form.is_valid()):

            obj = expenses()

            obj.month = form.cleaned_data['month']
            obj.year = form.cleaned_data['year']
            obj.factoryname = form.cleaned_data['factoryname']
            obj.bonus = form.cleaned_data['bonus']
            obj.carrying = form.cleaned_data['carrying']
            obj.earn = form.cleaned_data['earn']
            obj.electricity = form.cleaned_data['electricity']
            obj.epf = form.cleaned_data['epf']
            obj.rent = form.cleaned_data['rent']
            obj.supplies = form.cleaned_data['supplies']
            obj.food = form.cleaned_data['food']
            obj.fuel = form.cleaned_data['fuel']
            obj.cf = form.cleaned_data['cf']
            obj.frieght = form.cleaned_data['frieght']
            obj.insurence = form.cleaned_data['insurence']
            obj.labour = form.cleaned_data['labour']
            obj.land = form.cleaned_data['land']
            obj.medical = form.cleaned_data['medical']
            obj.miscellaneous = form.cleaned_data['miscellaneous']
            obj.repair = form.cleaned_data['repair']
            obj.tolls = form.cleaned_data['tolls']
            obj.transportation = form.cleaned_data['transportation']
            obj.wages = form.cleaned_data['wages']
            a = form.cleaned_data['bonus']
            b = form.cleaned_data['carrying']
            c = form.cleaned_data['earn']
            d = form.cleaned_data['electricity']
            e = form.cleaned_data['epf']
            f = form.cleaned_data['rent']
            h = form.cleaned_data['supplies']
            i = form.cleaned_data['food']
            j = form.cleaned_data['fuel']
            k = form.cleaned_data['cf']
            l = form.cleaned_data['frieght']
            m = form.cleaned_data['insurence']
            n = form.cleaned_data['labour']
            o = form.cleaned_data['land']
            p = form.cleaned_data['medical']
            q = form.cleaned_data['miscellaneous']
            r = form.cleaned_data['repair']
            s = form.cleaned_data['tolls']
            t = form.cleaned_data['transportation']

            u = (a+b+c+d+e+f+h+i+j+k+l+m+n+o+p+q+r+s+t)
            obj.total = u

            factoryname = form.cleaned_data['factoryname']
            month = form.cleaned_data['month']
            year = form.cleaned_data['year']
            g = cost.objects.all().filter(factoryname=factoryname)




            t = str(obj.month)
            d = str(obj.year)

            obj.save()
            return redirect('/profile2/check')



        else:
            messages.error(request, "Error")
    else:
        form = ABC2()
        return render(request, 'datas/profile.html', {'form': form})

    args = {'user': request.user}
    return render(request, 'datas/profile.html', args)


def check(request):


    return render(request, 'datas/check.html')

# Create your views here.
def minutes(request):
    if (request.method == 'POST'):
        form = query(request.POST)
        if (form.is_valid()):

            obj = minu()

            obj.month = form.cleaned_data['month']
            obj.year = form.cleaned_data['year']
            obj.day =form.cleaned_data['day']
            obj.minutes = form.cleaned_data['minutes']
            obj.line=form.cleaned_data['line']

            obj.save()
            return redirect('/profile2/check')



        else:
            messages.error(request, "Error")
    else:
        form = query()
        return render(request, 'datas/profile.html', {'form': form})


    args = {'user': request.user}
    return render(request, 'datas/profile.html', args)


def helper_func(month,year):

    a= minu.objects.all().filter(month = month,year = year)
    c=0
    for i in a:
        m = i.minutes
        c= c+m
    return(c)

def home(request):
    if request.method == 'POST':
        query_form = query2(request.POST)
        if (query_form.is_valid()):
            clean_query = query_form.cleaned_data
            factoryname = clean_query['factoryname']
            month = clean_query['month']
            year = clean_query['year']

            m = clean_query['line']
            w= 0
            z =0

            if (m == 'EP_1'):

                a= cost.objects.all().filter(factoryname = factoryname,month = month,year = year,line = m).values_list('EP_1_minutes')
                b =cost.objects.all().filter(factoryname = factoryname,month = month,year = year,line = m).values_list('EP_1_cost')
                for  j in  b:

                    z = j


            elif (m == 'EP_2'):
                a = cost.objects.all().filter(factoryname = factoryname,month = month,year = year,line = m).values_list('EP_2_minutes')
                b = cost.objects.all().filter(factoryname = factoryname,month = month,year = year,line = m).values_list('EP_2_cost')
                for  j in  b:

                    z = j
            elif (m == 'EP_3'):
                a = cost.objects.all().filter(factoryname = factoryname,month = month,year = year,line = m).values_list('EP_3_minutes')
                b = cost.objects.all().filter(factoryname = factoryname,month = month,year = year,line = m).values_list('EP_3_cost')
                for j in  b:

                    z = j
            elif (m == 'EP_4'):
                a = cost.objects.all().filter(factoryname=factoryname, month=month, year=year, line=m).values_list(
                    'EP_4_minutes')
                b = cost.objects.all().filter(factoryname=factoryname, month=month, year=year, line=m).values_list(
                    'EP_4_cost')
                for j in  b:

                    z = j


            elif (m == 'EP_5'):
                a = cost.objects.all().filter(factoryname=factoryname, month=month, year=year, line=m).values_list(
                    'EP_5_minutes')
                b = cost.objects.all().filter(factoryname=factoryname, month=month, year=year, line=m).values_list(
                    'EP_5_cost')
                for j in b:

                    z = j

            elif (m == 'EP_6'):
                a = cost.objects.all().filter(factoryname=factoryname, month=month, year=year, line=m).values_list(
                    'EP_6_minutes')
                b = cost.objects.all().filter(factoryname=factoryname, month=month, year=year, line=m).values_list(
                    'EP_6_cost')

                for  j in  b:

                    z = j

            elif (m == 'EP_7'):
                a = cost.objects.all().filter(factoryname=factoryname, month=month, year=year, line=m).values_list(
                    'EP_7_minutes')
                b = cost.objects.all().filter(factoryname=factoryname, month=month, year=year, line=m).values_list(
                    'EP_7_cost')
                for  j in  b:

                    z = j

            elif (m == 'EP_8'):
                a = cost.objects.all().filter(factoryname=factoryname, month=month, year=year, line=m).values_list(
                    'EP_8_minutes')
                b = cost.objects.all().filter(factoryname=factoryname, month=month, year=year, line=m).values_list(
                    'EP_8_cost')
                for  j in  b:

                    z = j

            elif (m == 'EP_9'):
                a = cost.objects.all().filter(factoryname=factoryname, month=month, year=year, line=m).values_list(
                    'EP_9_minutes')
                b = cost.objects.all().filter(factoryname=factoryname, month=month, year=year, line=m).values_list(
                    'EP_9_cost')
                for  j in  b:

                    z = j

            else :
                a = cost.objects.all().filter(factoryname=factoryname, month=month, year=year, line=m).values_list(
                    'EP_10_minutes')
                b = cost.objects.all().filter(factoryname=factoryname, month=month, year=year, line=m).values_list(
                    'EP_10_cost')
                for  j in  b:

                    z = j
            context = { 'cost': z,'factoryname':factoryname,'month':month,'year':year,'line':m}
            return render(request, 'datas/result.html', context)
            # return redirect('/result')

    else:
        query_form = query2()
        return render(request, 'datas/home.html', {'query_form': query_form})


