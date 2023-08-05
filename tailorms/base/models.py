from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=200,blank=True,null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)




    def __str__(self):
        return self.name


class FashionCompany(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    address =models.CharField(max_length=500, blank=True, null=True)
    logo = models.ImageField( blank=True, null=True)
    plan = models.CharField( max_length=50,default='basic', blank=True, null=True)
    wallet = models.DecimalField(max_digits=7,decimal_places=2, null=True, blank=True, default=0.0)

    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Tailor(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    company = models.ForeignKey(FashionCompany, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    wallet = models.DecimalField(max_digits=7,decimal_places=2, null=True, blank=True, default=0.0)
    total_work=models.IntegerField(default=0)
    total_pending_work=models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)


    def __str__(self):
        return self.name

class Customer(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(FashionCompany, on_delete=models.CASCADE,blank=True, null=True)
    name =  models.CharField(max_length=200 ,blank=True, null=True)
    email = models.CharField(max_length=200 ,blank=True, null=True)
    wallet = models.DecimalField(max_digits=7,decimal_places=2, null=True, blank=True, default=0.0)
    phone = models.CharField(max_length=20,blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    total_order=models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)


    def __str__(self):
        return self.profile.name

class Style(models.Model):
    company = models.ForeignKey(FashionCompany, on_delete=models.CASCADE,blank=True, null=True)
    image = models.ImageField( blank=True, null=True)
    description = models.TextField()
    gender = models.CharField(max_length=20, default='m' ,blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.description
    





class Work(models.Model):
    #profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    company = models.ForeignKey(FashionCompany, on_delete=models.CASCADE, blank=True, null=True)
    style = models.ForeignKey('Style', related_name='style', on_delete=models.CASCADE, blank=True, null=True)
    tailor =  models.ForeignKey(Tailor, related_name='tailor', on_delete=models.CASCADE,blank=True, null=True)
    customer = models.ForeignKey('Customer', related_name='customer', on_delete=models.CASCADE,blank=True, null=True)
    style_description = models.CharField(max_length=200, null=True, blank=True)
    tailor_name = models.CharField(max_length=200, null=True, blank=True)
    custormer_name = models.CharField(max_length=200, null=True, blank=True)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    measurement =models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True, default=0.0)
    isCompleted = models.BooleanField(default=False)
    isPaid =  models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.customer.name
    
    

    