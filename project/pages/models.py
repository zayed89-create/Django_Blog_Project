from django.db import models

# Create your models here.
class Female(models.Model):
    female_name=models.CharField(max_length=50,null=True) 
    def __str__(self):
       return  self.female_name
class Male (models.Model) :
    male_name= models.CharField(max_length=50,null=True)   
    girls= models.OneToOneField(Female,on_delete=models.CASCADE)
    def __str__(self):
       return  self.male_name



class Product(models.Model):
    title=models.CharField(max_length=50,null=True) 
    def __str__(self):
       return  self.title
class Video(models.Model):
    title=models.CharField(max_length=50,null=True) 
    def __str__(self):
       return  self.title

class User(models.Model):
    name=models.CharField(max_length=50,null=True)  
   
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
       return  self.name
class Username(models.Model):
    name=models.CharField(max_length=50,null=True)  
   
    watch=models.ManyToManyField(Video,null=True)
    def __str__(self):
       return  self.name
class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)