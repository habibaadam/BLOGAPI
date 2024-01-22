from django.shortcuts import render
from django.http import HttpResponse

"""Function presenting the blog home page"""
def blog_home(request):
    return HttpResponse('<h1>Blog Home</h1>')

"""Function presenting the blog about page"""
def blog_about(request):
    return HttpResponse('<h1>Blog About</h1>')
