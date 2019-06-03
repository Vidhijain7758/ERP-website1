from django.urls import path
from datas import views
from django.contrib.auth.views import login,logout

urlpatterns=[
path('',views.start,name='start'),
path('accounts/profile/home/',views.home,name='home'),
path('login1/', views.login1,  name='login1'),
path('login2/', views.login2, name='login2'),
path('login3/', views.login3, name='login3'),
path('login4/', views.login4, name='login4'),


path('accounts/profile/logout.html/', logout, {'template_name': 'datas/logout.html'}),
path('register/', views.register, name='register'),


path('profile/',views.profile,name = 'profile'),
path('profile1/',views.profile1,name = 'profile1'),
path('profile2/',views.profile2,name = 'profile2'),
path('profile3/',views.profile3,name = 'profile3'),

path('accounts/profile/home1/',views.home1,name='home1'),
path('accounts/profile/home2/',views.home2,name ='home2'),
path('accounts/profile/home3/',views.home3,name ='home3'),


path('accounts/profile/home/menu',views.menu,name='menu'),
path('accounts/profile/home/order',views.order,name='order'),
path('select1/',views.select1,name ='select1'),




path('order/<int:order_id>/', views.show, name='show'),


path('order/delete/<int:order_id>/', views.destroy, name='delete'),

path('product/new', views.new_product, name='new_product'),
path('product/delete/<int:product_id>/', views.destroy_product, name='delete_product')
        ]

