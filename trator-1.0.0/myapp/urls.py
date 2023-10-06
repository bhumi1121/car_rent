from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('client',views.client,name='client'),
    path('contact',views.contact,name='contact'),
    path('gallery',views.gallery,name='gallery'),
    path('services',views.services,name='services'),
    path('about',views.about,name='about'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('fpswd',views.fpswd,name='fpswd'),
    path('verify_otp',views.verify_otp,name='verify_otp'),
    path('set_pswd',views.set_pswd,name='set_pswd'),
    path('manager_index',views.manager_index,name='manager_index'),
    path('add_vehicle',views.add_vehicle,name='add_vehicle'),
    path('my_gallery',views.my_gallery,name='my_gallery'),
    path('Vehicle_details /<int:pk>',views.Vehicle_details,name='Vehicle_details'),
    path('update_vehicle/<int:pk>',views.update_vehicle,name='update_vehicle'),
    path('delete_vehicle/<int:pk>',views.delete_vehicle,name='delete_vehicle'),
    path('v_details /<int:pk>',views.v_details,name='v_details'),
   


]
