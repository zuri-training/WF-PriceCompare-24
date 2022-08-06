from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login_user/', views.login_user, name='login'),
    path('createaccount/', views.createaccount, name= 'createaccount'),
    path('documentation/', views.documentation, name='documentation'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('fashion/', views.fashion, name='fashion'),
    path('fashion/men/', views.fashionmen, name='fashionmen'),
    path('fashion/women/', views.fashionwomen, name='fashionwomen'),
    path('gadgets/', views.gadgets, name='gadget'),
    path('gadget/laptops/', views.laptop, name='laptops'),
    path('gadget/phones/', views.phone, name='phones'),
    path('gadget/tv/', views.tv, name='tv'),
    path('hair', views.hair, name='hairHomePage'),
    path('hair/humanhair', views.humanhair, name='humanhair'),
    path('hair/bonestraight/', views.bonestraight, name='bonestraight'),
    path('hair/accessories', views.accessories, name='hairaccessories'),


]