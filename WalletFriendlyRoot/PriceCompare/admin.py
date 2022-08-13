from django.contrib import admin
from .models import *
#from .models import PriceCompare

# Register your models here.
#admin.site.register(PriceCompare)

admin.site.register(Categories)
admin.site.register( Merchant)
admin.site.register( Product)