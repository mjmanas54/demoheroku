from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.index,name='home'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('search',views.search,name='search'),
    path('search2',views.search2,name='search2'),
    path('dealerinfo',views.dealerinfo,name='search2info'),
    path('contactdealer',views.contactdealer,name='contactdealer'),
]
