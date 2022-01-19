from django.db import models

# Create your models here.
class SalesPerson(models.Model):
    
    email=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)

    def __str__ (self):
        return self.username
class Category(models.Model):
    category_name=models.CharField(max_length=255)
    status=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    deleted=models.BooleanField(default=False)
    updated_at=models.DateTimeField(auto_now_add=False,blank=True,null=True)

    def __str__ (self):
        return self.category_name
 #Product MOdel
class Product(models.Model):
     category=models.ForeignKey(Category, on_delete=models.DO_NOTHING)
     product_web_name=models.CharField(max_length=255)
     product_code=models.CharField(max_length=255)
     status=models.BooleanField(default=True)
     created=models.DateTimeField(auto_now_add=True)
     deleted=models.BooleanField(default=False)
     updated_at=models.DateTimeField(auto_now_add=False,blank=True,null=True)

     def __str__ (self):
         return self.product_web_name
#Product Complain
class Complain(models.Model):
     details=models.TextField()
     status=models.BooleanField(default=True)
     created=models.DateTimeField(auto_now_add=True)
     deleted=models.BooleanField(default=False)
     updated_at=models.DateTimeField(auto_now_add=False,blank=True,null=True)
