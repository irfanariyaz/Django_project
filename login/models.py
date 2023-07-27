from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='subcat')

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Classifields(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE,null=True,blank=True)
    category = models.ForeignKey(Category,blank=True ,on_delete=models.CASCADE,null=True)
    subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE,null=True,blank=True)
    phone_no = models.CharField(max_length=20,null=True)


    def __str__(self):
        return self.title
    

    
