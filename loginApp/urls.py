from django.urls import path, include
from loginApp import views


app_name = "loginApp"
urlpatterns = [
    path('login/', views.adminLogin, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]
