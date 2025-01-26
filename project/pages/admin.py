from django.contrib import admin
from .models import Male,Female,User,Product,Username,Video,Login
# Register your models here.
admin.site.register(Female)
admin.site.register(Male)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Username)
admin.site.register(Video)
admin.site.register(Login)
admin.site.site_header='zayed'
admin.site.site_title='zayed'