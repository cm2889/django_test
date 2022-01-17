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
    updated_by=models.IntegerField(null=True)

    def __str__ (self):
        return self.name