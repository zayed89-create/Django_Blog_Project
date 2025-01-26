from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.
def all_posts(request):
    all_posts=Post.objects.all()
    context={
        'all_posts':all_posts
    }
    return render( request,'all_posts.html',context)



def post(request,id):
    post= get_object_or_404(Post,id=id)
    return render(request,'details.html',{'post':post})