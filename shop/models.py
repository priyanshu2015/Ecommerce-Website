from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import UserManager
from django.core.validators import RegexValidator
import datetime

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255,blank=True, null=True, default=None)
    phone_regex = RegexValidator( regex = r'^\+?1?\d{10}$',message = "Phone number must be entered in proper format in 10 digits.")#the format: '+999999999'. Up to 14 digits allowed.")
    user_phone = models.CharField(validators = [phone_regex], max_length=15)
    user_email = models.EmailField('email address', unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_email_verified = models.BooleanField(default=False)
    is_premium_activated = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.user_email

# Create your models here.
# create a database schema structure
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    # function so that in database items added to database are shown with their name
    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
    amount = models.IntegerField(default=0)
    razorpayid = models.CharField(max_length=255,default="")
    razorpaypaymentid = models.CharField(max_length=255,default="")
    razorpaysignature = models.CharField(max_length=255, default="")


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
