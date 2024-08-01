from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from modBlog.models import Blog


# Create your views here.

def add(request): 
  if request.method == 'POST':
    name = request.POST['name']
    title = request.POST['title']
    categories = request.POST['categories']
    tag = request.POST['tag']
    image = request.FILES['image']
    content = request.POST['content']

    Blog.objects.create(name=name, title=title, categories=categories, tag=tag, image=image, content=content)
    return redirect('index') #reverse path name=home
  return render(request, 'add.html')
  

  
def editblog(request, pk):
  objEdit = get_object_or_404(Blog, pk=pk)
  if request.method == 'POST':
    objEdit.name = request.POST.get('name')
    objEdit.title = request.POST.get('title')
    objEdit.categories = request.POST.get('categories')
    objEdit.tag = request.POST.get('tag')
    objEdit.image = request.FILES.get('image')
    objEdit.content = request.POST.get('content')

    objEdit.save()
    return redirect( 'index' )
  else:
    context = {
      'objEdit': objEdit,
    }
  return render(request, 'edit.html', context)



def deleteblog(request, pk):
  objDelete = get_object_or_404(Blog, pk=pk)
  objDelete.delete()
  return redirect('index')

def about(request): 
  return render(request, 'about.html')
  
def contact(request):
  return render(request, 'contact.html' )

def privacypolicy(request):
  return render(request, 'privacypolicy.html' )

def termsconditions(request):
  return render(request, 'termsconditions.html')

def login(request):
  return render(request, 'login.html')

def signup(reuqest):
  return render(reuqest, 'signup.html')

def continueread(request):
  return render(request, 'continueread.html' )
  