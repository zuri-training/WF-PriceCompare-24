from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('fashion/', views.fashion, name='fashion.html'),
    path('fashion/men/', views.fashionmen, name='fashionmen.html'),
    path('fashion/women/', views.fashionwomen, name='fashionwomen.html'),
    path('gadgets/', views.gadgets, name='gadget.html'),
    path('gadget/laptops/', views.laptop, name='laptops.html'),
    path('gadget/phones/', views.phone, name='phones.html'),
    path('gadget/tv/', views.tv, name='tv.html'),
    path('hair', views.hair, name='hairHomPage.html'),
    path('hair/humanhair', views.humanhair, name='humanhair.html'),
    path('hair/bonestraight/', views.bonestraight, name='bonestraight.html'),
    path('hair/accessories', views.accessories, name='hairaccessories.html'),


]