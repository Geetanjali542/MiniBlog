from django.http import HttpResponse
from django.shortcuts import render
from modBlog.models import Blog



def index(request):
    blog_data = Blog.objects.all() #Employee is from modals.py of the employee app
    context = {
        "blog":blog_data,
    }
    return render(request, 'index-list.html', context)


    