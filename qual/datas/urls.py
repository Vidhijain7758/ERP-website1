from django.urls import path
from datas import views
from django.contrib.auth.views import login,logout

urlpatterns=[
path('home/',views.home,name='home'),
path('login/', login, {'template_name': 'datas/login.html'}, name='login'),
path('accounts/profile/logout.html/', logout, {'template_name': 'datas/logout.html'}),
path('register/', views.register, name='register'),
path('accounts/profile/', views.profile, name='profile'),
path('profile/check/',views.check,name='check'),
#path('home2/',views.home2,name='home2'),
    path('profile/update/<int:pk>',views.update.as_view(),name='update')
]