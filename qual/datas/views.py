from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth import authenticate
from datas.forms import CustomUserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import quality,total
from .forms import LoginForm,ABC,QueryForm ,QueryForm2
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg, Count, Max, Min, Sum
import matplotlib.pyplot as plt
import datetime
from matplotlib.pyplot import figure, title, bar
import numpy as np
import mpld3
from django.views.generic import UpdateView
import matplotlib

# Create your views here.
def loginpage(request):
    myform=LoginForm(request.POST or None)
    if myform.is_valid():
        usern=myform.cleaned_data.get("username")
        passw=myform.cleaned_data.get("password")
        user=authenticate(username=usern,password=passw)
        if user:
            return redirect('/profile')
        else:
            messages.error(request, "Error")
    return render(request,"datas/login.html",{"form":myform})

def register(request):
    if (request.method=='POST'):
        form =CustomUserCreationForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('/login')
        else:
            messages.error(request, "Error")
    else:
        form= CustomUserCreationForm()

    args={'form':form}
    return render(request,'datas/signup.html',args)

def home(request):


    dhu=[]
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if(form.is_valid()):
            clean_query = form.cleaned_data


            name1 = User.objects.get(id=request.user.id).username
            factoryname = form.cleaned_data.get('factoryname').lower()
            category = form.cleaned_data.get('category').lower()
            sub_category = form.cleaned_data.get('sub_category').lower()
            department = form.cleaned_data.get('department').lower()
            section = form.cleaned_data.get('section').lower()
            item_no = form.cleaned_data.get('item_no')
            style_name = form.cleaned_data.get('style_name').lower()
            style_no = form.cleaned_data.get('style_no')
            dhu_date = form.cleaned_data.get('for_date')
            r = quality()

            e = quality.objects.all().filter(name=name1, factoryname=factoryname, category=category,
                                                      sub_category=sub_category,
                                                      department=department, section=section, item_no=item_no,
                                                      style_name=style_name, style_number=style_no
                                                      , date=dhu_date)

            #e = quality.objects.all().filter(date = dhu_date)
            for i in e:
                dhu.append(i.EP_1)
                dhu.append(i.EP_2)
                dhu.append(i.EP_3)
                dhu.append(i.EP_4)
                dhu.append(i.EP_5)
                dhu.append(i.EP_6)
                dhu.append(i.EP_7)
                dhu.append(i.EP_8)
                dhu.append(i.EP_9)
                dhu.append(i.EP_10)
                dhu.append(i.EP_11)
                dhu.append(i.EP_12)
                dhu.append(i.EP_13)
                dhu.append(i.EP_14)
                dhu.append(i.EP_15)
                dhu.append(i.EP_16)
                dhu.append(i.EP_17)
                dhu.append(i.EP_18)
                dhu.append(i.EP_19)
                dhu.append(i.EP_20)
                dhu.append(i.EP_21)
                dhu.append(i.EP_22)
                dhu.append(i.EP_23)
                dhu.append(i.EP_24)



            mpl_figure = figure(1, figsize=(12, 6))


            xvalues=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)
            y0=float(dhu[0])
            y1 = dhu[1]
            y2 = dhu[2]
            y3 = dhu[3]
            y4 = dhu[4]
            y5 = dhu[5]
            y6 = dhu[6]
            y7 = dhu[7]
            y8 = dhu[8]
            y9 = dhu[9]
            y10 = dhu[10]
            y11 = dhu[11]
            y12 = dhu[12]
            y13 = dhu[13]
            y14 = dhu[14]
            y15 = dhu[15]
            y16 = dhu[16]
            y17 = dhu[17]
            y18 = dhu[18]
            y19 = dhu[19]
            y20 = dhu[20]
            y21=dhu[21]
            y22 = dhu[22]
            y23 = dhu[23]


            yvalues=(y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20,y21,y22,y23)
            width = 0.5

            labels = ('EP1', 'EP2', 'EP3', 'EP4', 'EP5', 'EP6', 'EP7', 'EP8', 'EP9', 'EP10', 'EP11', 'EP12', 'EP13', 'EP14','EP15','EP16', 'EP17','EP18','EP19','EP20','EP21','EP22','EP23','EP24')
            plt.plot(xvalues,yvalues,width)
            plt.xlabel('LINE NUMBER')
            plt.xticks(xvalues,labels)
            plt.ylabel('DHU OF EACH LINE')
            plt.title('graph for the DHU')
            ax = mpl_figure.add_subplot(111)
            for xy in zip( xvalues,yvalues):
                ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')

            fig_html = mpld3.fig_to_html(mpl_figure)
            plt.clf()


            return render(request,'datas/result.html',{'figure':fig_html},{'e':e})




    else:
        query_form = QueryForm()
        return render(request, 'datas/home.html', {'query_form': query_form})





def profile(request):
    if (request.method == 'POST'):
        form = ABC(request.POST)
        #form2 =CustomUserCreationForm(request.POST)

        if (form.is_valid()):
            m = form.cleaned_data.get('line_no')

            name1 = User.objects.get(id=request.user.id).username
            factoryname = form.cleaned_data.get('factoryname').lower()
            category = form.cleaned_data.get('category').lower()
            sub_category = form.cleaned_data.get('sub_category').lower()
            department = form.cleaned_data.get('department').lower()
            section = form.cleaned_data.get('section').lower()
            item_no = form.cleaned_data.get('item_no')
            style_name = form.cleaned_data.get('style_name').lower()
            style_no = form.cleaned_data.get('style_no')
            date = form.cleaned_data.get('date')
            r = quality()
            try:

                obj1 = quality().objects.all().filter(name = name1,factoryname =factoryname, category = category,sub_category =sub_category,
                         department =department,section =section,item_no =item_no,style_name =style_name,style_number =style_no
                                              ,date = date )



                a1 = form.cleaned_data.get('total_defects')
                b1 = form.cleaned_data.get('total_checked')
                c1 = form.cleaned_data.get('total_checked')
                ep0 = (a1 / b1) * 100



                if (m == 'EP_0'):
                    obj1.update(EP_0 = ep0)
                elif (m == 'EP_1'):
                    obj1.update(EP_1 = ep0)
                elif (m == 'EP_2'):
                    obj1.update(EP_2 = ep0)
                elif (m == 'EP_3'):
                    obj1.update(EP_3 =ep0)
                elif (m == 'EP_4'):
                    obj1.update(EP_4 = ep0)
                elif (m == 'EP_5'):
                    obj1.update(EP_5 = ep0)
                elif (m == 'EP_6'):
                    obj1.update(EP_6 = ep0)
                elif (m == 'EP_7'):
                    obj1.update(EP_7 = ep0)
                elif (m == 'EP_8'):
                    obj1.update(EP_8 = ep0)
                elif (m == 'EP_9'):
                    obj1.update(EP_9 = ep0)
                elif (m == 'EP_10'):
                    obj1.update(EP_10 = ep0)
                elif (m == 'EP_11'):
                    obj1.update(EP_11 = ep0)
                elif (m == 'EP_12'):
                    obj1.update(EP_12 = ep0)
                elif (m == 'EP_13'):
                    obj1.update(EP_13 = ep0)
                elif (m == 'EP_14'):
                    obj1.update(EP_14 = ep0)
                elif (m == 'EP_15'):
                    obj1.update(EP1 = ep0)
                elif (m == 'EP_16'):
                    obj1.update(EP_16 = ep0)
                elif (m == 'EP_17'):
                    obj1.update(EP_17 = ep0)
                elif (m == 'EP_18'):
                    obj1.update(EP_18 = ep0)
                elif (m == 'EP_19'):
                    obj1.update(EP_19 = ep0)
                elif (m == 'EP_20'):
                    obj1.update(EP_20 = ep0)
                elif (m == 'EP_21'):
                    obj1.update(EP_21 = ep0)
                elif (m == 'EP_22'):
                    obj1.update(EP_22 = ep0)
                elif (m == 'EP_23'):
                    obj1.update(EP_23 = ep0)
                else:
                    obj1.update(EP_24 = ep0)

                return redirect('/profile/check')






            except AttributeError:


                a1 = form.cleaned_data.get('total_defects')
                b1 = form.cleaned_data.get('total_checked')
                c1 = form.cleaned_data.get('total_checked')
                EP0 = (a1 / b1) * 100
                r.date = form.cleaned_data['Date']

                if (m == 'EP_0'):
                    r.EP_0 = EP0
                elif (m == 'EP_1'):
                    r.EP_1 = EP0
                elif (m == 'EP_2'):
                    r.EP_2 = EP0
                elif (m == 'EP_3'):
                    r.EP_3 = EP0
                elif (m == 'EP_4'):
                    r.EP_4 = EP0
                elif (m == 'EP_5'):
                    r.EP_5 = EP0
                elif (m == 'EP_6'):
                    r.EP_6 = EP0
                elif (m == 'EP_7'):
                    r.EP_7 = EP0
                elif (m == 'EP_8'):
                    r.EP_8 = EP0
                elif (m == 'EP_9'):
                    r.EP_9 = EP0
                elif (m == 'EP_10'):
                    r.EP_10 = EP0
                elif (m == 'EP_11'):
                    r.EP_11 = EP0
                elif (m == 'EP_12'):
                    r.EP_12 = EP0
                elif (m == 'EP_13'):
                    r.EP_13 = EP0
                elif (m == 'EP_14'):
                    r.EP_14 = EP0
                elif (m == 'EP_15'):
                    r.EP1 = EP0
                elif (m == 'EP_16'):
                    r.EP_16 = EP0
                elif (m == 'EP_17'):
                    r.EP_17 = EP0
                elif (m == 'EP_18'):
                    r.EP_18 = EP0
                elif (m == 'EP_19'):
                    r.EP_19 = EP0
                elif (m == 'EP_20'):
                    r.EP_20 = EP0
                elif (m == 'EP_21'):
                    r.EP_21 = EP0
                elif (m == 'EP_22'):
                    r.EP_22 = EP0
                elif (m == 'EP_23'):
                    r.EP_23 = EP0
                else:
                    r.EP_24 = EP0
                r.name = name1

                r.factoryname = factoryname
                r.category =category
                r.sub_category =sub_category
                r.department = department
                r.section = section
                r.item_no = item_no
                r.style_name = style_name
                r.style_number = style_no
                r.save()
                return redirect('/profile/check')

        else:
            messages.error(request, "Error")
    else:
        form = ABC()
        return render(request,'datas/profile.html',{'form':form})

    args={'user':request.user}
    return render(request,'datas/profile.html',args)

def check(request):
    return render(request,'datas/check.html')





def helper_start_date(start_date):
    '''Takes in a datetime object, which may either be typecast from a user-supplied
    date string or the earliest date found in the data table. Returns the date as a string.'''
    if not start_date:
        start_date_obj = quality.objects.all().aggregate(Min('date'))
        start_date = start_date_obj['date__min']
    else:
        start_date = start_date

    return (start_date)


def helper_end_date(end_date):
    '''Takes in a datetime object, which may either be typecast from a user-supplied
    date string or the latest date found in the data table. Returns the date as a string.'''

    if not end_date:
        end_date_obj = quality.objects.all().aggregate(Max('date'))
        end_date = end_date_obj['date__max']
    else:
        end_date = end_date

    return (end_date)


def helper_min_date():
    '''Does not require an input. Returns the earliest date in the data table.'''

    min_date_obj = quality.objects.all().aggregate(Min('date'))
    min_date_str = min_date_obj['date__min']

    return (min_date_str)


def helper_max_date():
    '''Does not require an input. Returns the latest date in the data table.'''

    max_date_obj = quality.objects.all().aggregate(Max('date'))
    max_date_str = max_date_obj['date__max']

    return (max_date_str)


'''def home2(request):
    w=[]
    if request.method == 'POST':
        query_form = QueryForm2(request.POST)
        if(query_form.is_valid()):
            clean_query = query_form.cleaned_data
            w=[]
            line = query_form.cleaned_data.get('line_no')

            factoryname = query_form.cleaned_data.get('factoryname')
            category = query_form.cleaned_data.get('category')
            sub_category = query_form.cleaned_data.get('sub_category')
            department = query_form.cleaned_data.get('department')
            section = query_form.cleaned_data.get('section')
            item_no = query_form.cleaned_data.get('item_no')
            style_name = query_form.cleaned_data.get('style_name')
            style_no = query_form.cleaned_data.get('style_no')
            z= quality.objects.filter( factoryname =factoryname, category =category,sub_category =sub_category,department =department,section =section,item_no =item_no,style_name =style_name,style_number =style_no)

            da =[]
            dhu =[]
            for i in z:
                y = i.date
                da.append(y)
                x = i.query_form.cleaned_data.get('line_no')
                dhu.append(x)


            

            return render(request, 'datas/result2.html', {'date' : da } ,{'dhu' :dhu})
        else:
            messages.error(request, "Error")



    else:
        query_form = QueryForm2()
        return render(request, 'datas/home.html', {'query_form': query_form})
'''
class update(UpdateView):
    model = quality

    fields = ('name', 'factoryname', 'category', 'sub_category', 'department', 'section', 'item_no', 'style_name',
                  'style_number', 'date','EP_1','EP_2','EP_3','EP_4','EP_5','EP_6','EP_7','EP_8','EP_9','EP_10','EP_11','EP_12','EP_13','EP_14','EP_15','EP_16','EP_17','EP_18','EP_19','EP_20','EP_21','EP_22','EP_23','EP_24')


    template_name = "datas/profile.html"
    success_url = "/profile/check"


def helpe():
    a=

