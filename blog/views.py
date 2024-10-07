from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'Author': 'ArnoldM',
        'Title': 'Blog Post 1',
        'Content': 'This is my First Post!!!',
        'date_posted': 'Sept 26, 2024'      
    },
    {
        'Author': 'Cesar',
        'Title': 'Blog Post 2',
        'Content': 'This is my Second Post!!!',
        'date_posted': 'Sept 26, 2024'      
    },
     {
        'Author': 'BC',
        'Title': 'Blog Post 3',
        'Content': 'This is my Third Post!!!',
        'date_posted': 'Sept 26, 2024'      
    }
]

def home(request):
    context = {
        'posts': posts
    }
        
    #return HttpResponse('<h1> WELCOME HOME !!! </h1>')
    return render(request, 'blog/home.html', context)

def about(request):
    #return HttpResponse('<h1> THIS IS ABOUT PAGE </h1>') 
    return render(request, 'blog/about.html')