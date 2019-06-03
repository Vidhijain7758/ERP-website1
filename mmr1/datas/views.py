

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth import authenticate
from datas.forms import CustomUserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import ie
from .forms import LoginForm, ABC1,query
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
def loginpage(request):
    myform = LoginForm(request.POST or None)
    if myform.is_valid():
        status = request.User.last_name
        usern = myform.cleaned_data.get("username")
        passw = myform.cleaned_data.get("password")

        user = authenticate(username=usern, password=passw)
        if user:
            return redirect("/profile")
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



def profile(request):
    if (request.method == 'POST'):
        form = ABC1(request.POST)
        if (form.is_valid()):

            obj = ie()

            obj.month = form.cleaned_data['month']
            obj.year = form.cleaned_data['year']
            obj.sampling_bud =form.cleaned_data['sampling_bud']
            obj.sampling_actual = form.cleaned_data['sampling_actual']
            obj.no_lines = form.cleaned_data['no_lines']
            obj.machines_line = form.cleaned_data['machines_line']
            obj.machine_oper = form.cleaned_data['machine_oper']
            obj.pattern_bud = form.cleaned_data['pattern_bud']
            obj.sampling_bud = form.cleaned_data['sampling_bud']
            obj.sampling_actual = form.cleaned_data['sampling_actual']
            obj.no_lines = form.cleaned_data['no_lines']
            obj.machines_line = form.cleaned_data['machines_line']
            obj.machine_oper = form.cleaned_data['machine_oper']
            obj.pattern_bud = form.cleaned_data['pattern_bud']
            obj.pattern_actual = form.cleaned_data['pattern_actual']
            obj.fabric_bud  = form.cleaned_data['fabric_bud']
            obj.fabric_actual = form.cleaned_data['fabric_actual']
            obj.trim_bud = form.cleaned_data['trim_bud']
            obj.trim_actual = form.cleaned_data['trim_actual']
            obj.cutting_bud = form.cleaned_data['cutting_bud']
            obj.cutting_actual = form.cleaned_data['cutting_actual']
            obj.sewing_bud = form.cleaned_data['sewing_bud']
            obj.sewing_actual = form.cleaned_data['sewing_actual']
            obj.ware_bud = form.cleaned_data['ware_bud']
            obj.ware_actual = form.cleaned_data['ware_actual']
            obj.planning_bud = form.cleaned_data['planning_bud']
            obj.planning_actual = form.cleaned_data['planning_actual']
            obj.ie_bud = form.cleaned_data['ie_bud']
            obj.ie_actual = form.cleaned_data['ie_actual']
            obj.maintainance_bud = form.cleaned_data['maintainance_bud']
            obj.maintainance_actual = form.cleaned_data['maintainance_actual']




            x = form.cleaned_data['sampling_bud']
            y = form.cleaned_data['sampling_actual']

            z = form.cleaned_data['pattern_bud']
            u = form.cleaned_data['pattern_actual']
            e = form.cleaned_data['fabric_bud']
            f = form.cleaned_data['fabric_actual']
            g = form.cleaned_data['trim_bud']
            h = form.cleaned_data['trim_actual']
            i = form.cleaned_data['cutting_bud']
            j = form.cleaned_data['cutting_actual']
            k = form.cleaned_data['sewing_bud']
            l = form.cleaned_data['sewing_actual']
            m = form.cleaned_data['ware_bud']
            n = form.cleaned_data['ware_actual']
            o = form.cleaned_data['planning_bud']
            p = form.cleaned_data['planning_actual']
            q = form.cleaned_data['ie_bud']
            r = form.cleaned_data['ie_actual']
            s = form.cleaned_data['maintainance_bud']
            t = form.cleaned_data['maintainance_bud']

            man_budgeted = (x+z+e+g+i+k+m+o+q+s)
            man_actual = (y+u+f+h+j+l+n+p+r+t)

            c = form.cleaned_data['no_lines']
            d = form.cleaned_data['machines_line']
            e = form.cleaned_data['machine_oper']
            mmr_budgeted = man_budgeted / (c * d)
            mmr_actual = man_actual / e
            obj.mmr_actual = mmr_actual
            obj.mmr_budgeted = mmr_budgeted
            month = form.cleaned_data['month']
            year = form.cleaned_data['year']










            g = ie.objects.all().filter(year =year)

            d = str(obj.month)
            c = 0
            for i in g:
                if (str(i.month) == month and str(i.year) == year):
                    c = c + 1
            if (c == 0):
                obj.save()
                return redirect('/profile/check')
            else:
                c = 0
                return redirect('/profile')



        else:
            messages.error(request, "Error")
    else:
        form = ABC1()
        return render(request, 'datas/profile.html', {'form': form})

    args = {'user': request.user}
    return render(request, 'datas/profile.html', args)

def home(request):
    if request.method == 'POST':
        query_form = query(request.POST)
        if (query_form.is_valid()):
            clean_query = query_form.cleaned_data




            month = clean_query['month']
            year = clean_query['year']

            output = ie.objects.all().filter(month = month,year = year)
            a=e=f=g=h=i=j=k=l=m=n=p=q=r=s=t=u=v=w=x=y=z=c=d= 0
            for o in output:
                e = o.sampling_bud
                f = o.sampling_actual
                j = o.pattern_bud
                g = o.pattern_actual
                k = o.fabric_bud
                l = o.fabric_actual
                m = o.trim_bud
                n = o.trim_actual
                a = o.cutting_bud
                p = o.cutting_actual
                q = o.sewing_bud
                r = o.sewing_actual
                s = o.ware_bud
                t = o.ware_actual
                u = o.planning_bud
                v = o.planning_actual
                w = o.ie_bud
                x = o.ie_actual
                y = o.maintainance_bud
                z = o.maintainance_actual
                c = o.no_lines
                d = o.machines_line
                e = o.machine_oper
            man_budgeted = (e + j + k + m + a + q + s + u + w + y)
            man_actual = (f + g + l + n + p + r + t + v + x + z)



            mmr_budgeted = man_budgeted / (c * d)
            mmr_actual = man_actual / e

            return render(request,'datas/result.html',{'output' :output,'month':month,'year':year,'mmr_budgeted':mmr_budgeted,'mmr_actual' : mmr_actual,'total1': man_budgeted,'total2':man_actual })

            # return redirect('/result')

    else:
        query_form = query()
        return render(request, 'datas/home.html', {'query_form': query_form})


def home1(request):

            output = ie.objects.all()

            return render(request,'datas/home1.html',{'output' :output})
            # return redirect('/result')

def check(request):

    return render(request, 'datas/check.html')


def helper(output):
    monthly =0.0
    a = 0.0
    b =0.0
    for i in output:
        a  = a + i.man_budgeted


    return a

def helper2(output):
    monthly = 0.0
    a = 0.0
    b = 0.0
    for i in output:
        b = a + i.man_actual

    return b