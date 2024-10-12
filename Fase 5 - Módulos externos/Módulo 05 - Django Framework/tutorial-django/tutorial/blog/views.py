from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    # Variables de contexto para pasar datos al template
    return render(request, "blog/home.html",{'posts':posts})



def post(request, id):
    post = Post.objects.get(id = id)
    # Variables de contexto para pasar datos al template
    return render(request, "blog/post.html",{'post':post})