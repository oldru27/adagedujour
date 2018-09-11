from django.shortcuts import render, get_object_or_404
from .models import blog2
from .models import blog2

# Create your views here.

def listblog(request):
    blogs = blog2.objects #transformer en object une instance blog
    return render(request,'blog/listblog.html', {'blogs_a_injecter': blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(blog2, pk=blog_id)
    return render(request,'blog/detail.html',{'blog': detailblog})