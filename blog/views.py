from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Create your views here.


# Create your views here.
def index(request):
    if request.method == "POST":
        heading = request.POST.get('heading','')
        blog = request.POST.get('blog','')
        image = request.POST.get('image','')
        blog_ins = Blog(heading = heading, blog = blog)
        blog_ins.save()
        blogs = Blog.objects.all()
        return render(request,'blog/index.html', {'blogs':blogs})
    blogs = Blog.objects.all()
    return render(request,'blog/index.html', {'blogs':blogs})
