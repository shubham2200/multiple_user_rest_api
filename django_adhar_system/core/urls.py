
from django.contrib import admin
from django.urls import path ,include
from .views import *
urlpatterns = [
    path('managersignup/',managerSignupView.as_view()),
    path('staffsignup/',StaffSignupView.as_view()),
    path('CostumAuth/',CostumAuth.as_view() , name='auth_token'),
    path('logout/',LogoutView.as_view() , name='logout'),
    path('ManagerDashboard/',OnlyManagerView.as_view() , name='ManagerDashboard'),
    path('StaffDashboard/',OnlyStaffView.as_view() , name='StaffDashboard'),
    path('CreateReadManager/',CreateReadManager.as_view() , name='CreateReadManager'),
    path('CreateReadManagerDetails/<int:pk>/',CreateReadManagerDetails.as_view() , name='CreateReadManagerDetails'),
    path('StaffOnlySee/',StaffOnlySee.as_view() , name='StaffOnlySee'),




    

]
