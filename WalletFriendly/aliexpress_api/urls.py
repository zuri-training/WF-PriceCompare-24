from django.urls import path
from . import views


app_name = "aliexpress_api"


urlpatterns = [
    path('', views.product, name = 'aliexpress')

]
