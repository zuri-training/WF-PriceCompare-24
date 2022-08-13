from django.db import models
from collections import UserString
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

# class Price(models.Model):
#        product = models.CharField(max_length=50, blank = True, null = True)
#        minPrice = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(2000.0)])
#        category = models.CharField(max_length=50)

#        def __str__(self):
#              return self.name


#  title = models.CharField(max_length=100)
   #  content = models.TextField(max_length= 1000)
   #  date_posted = models.DateTimeField(default=timezone.now)
   #  author = models.ForeignKey(User, on_delete=models.CASCADE)
   #  phone = models.CharField(max_length=10, default="Integer")
   #  def __str__(self):
   #      return self.title

   #  def get_absolute_url(self):
   #      return reverse('post-detail', kwargs={'pk':self.pk})

# categories: id, name, type, product type,category type.
# merchant: category_id, Product_id, merchant_name, merchant_id
# product: Product_id, category_id, product name, price
# favourites: user_id, Product_id, category_id, date.
# Export socials, email, userid, product id.
# comments: userid, Product_id, content, date


# Users: merchant_id, merchant_name,category_id, product id.

class Categories(models.Model):

   name = models.CharField(max_length=255)
   time = models.DateTimeField()

   def __str__(self):
      return self.name
   
   

class Merchant(models.Model):
   
   name = models.CharField(max_length=100)

   def __str__(self):
      return self.name


class Product(models.Model):
   
   name = models.TextField()
   price = models.FloatField()
   stars = models.CharField(max_length=50)
   ratings = models.SmallIntegerField()
   categories = models.ForeignKey(Categories,on_delete=models.CASCADE)
   vendor = models.ForeignKey(Merchant ,on_delete=models.CASCADE )
   image = models.CharField(max_length= 5000, null=True, blank=True)

   def __str__(self):
      return self.name

