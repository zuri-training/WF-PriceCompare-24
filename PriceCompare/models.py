import email
from django.db import models
from django.contrib.auth import get_user_model
#from collections import UserString
#from django.utils import timezone
#from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

# class Categories(models.Model):

#    name = models.CharField(max_length=255)
#    time = models.DateTimeField()

#    def __str__(self):
#       return self.name
   
   

# class Merchant(models.Model):
   
#    name = models.CharField(max_length=100)

#    def __str__(self):
#       return self.name


# class Product(models.Model):
   
#    name = models.TextField()
#    price = models.FloatField()
#    stars = models.CharField(max_length=50)
#    ratings = models.SmallIntegerField()
#    categories = models.ForeignKey(Categories,on_delete=models.CASCADE)
#    vendor = models.ForeignKey(Merchant ,on_delete=models.CASCADE )
#    image = models.CharField(max_length= 5000, null=True, blank=True)

#    def __str__(self):
#       return self.name

class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   first_name = models.CharField(max_length=100, blank=True)
   last_name = models.CharField(max_length=100, blank=True)
   email = models.EmailField(max_length=150)
   phone_number = models.PositiveBigIntegerField(blank=True)

   def __str__(self):
      return self.user.username


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwards):
   if created:
      Profile.objects.create(user=instance)
   instance.profile.save