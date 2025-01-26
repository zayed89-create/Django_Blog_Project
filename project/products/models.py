from django.db import models
from datetime import datetime

# Create your models here.
class Product (models.Model):

    x = [
        ('phone','phone'),
        ('computer','computer'),
    ]
    name = models.CharField(max_length=50,default='name',verbose_name='title')
    content = models.TextField ( null= True,blank= True,verbose_name='description')
    price = models.DecimalField(max_digits=6,decimal_places=2,default=444)
    image = models.ImageField(upload_to='photos/%y/%m/%d',default='photos/24/11/22/73-alx-aice-ai-career-essentials-certificate-zayed-ibrahim.png')
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=50,null= True,blank= True,choices=x)


    def __str__(self):
        return self.name
    class Meta:
       ordering = ['-name']
class Test(models.Model):
    date = models.DateField()
    time = models.TimeField(null = True)
    datetime = models.DateTimeField(default=datetime.now)



