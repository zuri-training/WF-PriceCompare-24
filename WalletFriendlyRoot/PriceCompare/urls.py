from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Login.html/', views.login_user, name='login'),
    path('createAccount.html/', views.createaccount, name= 'createaccount'),
    path('documentation.html/', views.documentation, name='documentation'),
    path('forgotPassword.html/', views.forgotpassword, name='forgotpassword'),
    path('fashion.html/', views.fashion, name='fashion'),
    path('fashionMen.html', views.fashionmen, name='fashionmen'),
    path('fashionMenAuth.html/', views.fashionmenauth, name='fashionmen'),
    path('fashionWomen.html/', views.fashionwomen, name='fashionwomen'),
    path('gadgetHomepage.html/', views.gadgets, name='gadget'),
    path('gadgetLaptops.html/', views.laptop, name='laptops'),
    path('gadgetPhones.html/', views.phone, name='phones'),
    path('gadgettv.html/', views.tv, name='tv'),
    path('hairHomePage.html/', views.hair, name='hairHomePage'),
    path('humanHair.html/', views.humanhair, name='humanhair'),
    path('humanHairAuth.html/', views.humanhairauth, name='humanhair'),
    path('boneStraight.html/', views.bonestraight, name='bonestraight'),
    path('hairAccessories.html', views.accessories, name='hairaccessories'),
    path('hairAccessoriesAuth.html/', views.accessoriesauth, name='hairaccessories'),
    path('compareGadget.html/', views.comparegadget, 'comparegadget'),

]