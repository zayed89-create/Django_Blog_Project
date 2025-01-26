from django.urls import path

from . import views 

app_name='Post'

urlpatterns=[
    path('',views.all_posts,name='all_posts'),
    url(r'\?id=\d+$',views.post,name='post'),
 
]