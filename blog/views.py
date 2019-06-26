from django.shortcuts import render

from .models import Blog 

def allblogs(request):
    jobs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blog': jobs})
