from django.urls import path
from datas import views
from django.contrib.auth.views import login,logout

urlpatterns=[
path('home/',views.home,name='home'),
path('login/', login, {'template_name': 'datas/login.html'}, name='login'),
path('accounts/profile/logout.html/', logout, {'template_name': 'datas/logout.html'}),
path('accounts/profile2/logout.html/', logout, {'template_name': 'datas/logout.html'}),
path('register/', views.register, name='register'),
path('accounts/profile/', views.profile1, name='profile'),
path('profile2/', views.profile2, name='profile2'),
path('profile1/check/',views.check,name='check'),
path('profile2/check/',views.check,name='check'),
path('minutes/',views.minutes,name = 'minutes')
]