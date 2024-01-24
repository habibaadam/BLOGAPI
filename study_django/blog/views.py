from django.shortcuts import render

"""trying with dummy data"""

posts = [
    {
        'author': 'HabieM',
        'title':'Blog Post 1',
        'content': 'First post on here!',
        'date_posted': 'May 5, 2021'
    },
    {
        'author': 'MansiBoo',
        'title': 'Blog Post 2',
        'content': 'I was dragged here not by my will',
        'date_posted': 'May 6, 2021'
    },
    {
        'author': 'Babo',
        'title': 'Blog Post 3',
        'content': 'Looks basicc!',
        'date_posted': 'May 6, 2021'
    },
    {
        'author': 'Amor',
        'title': 'Blog Post 4',
        'content': 'Que sera, sera',
        'date_posted': 'May 7, 2021'
    }
]

"""Function presenting the blog home page"""
def blog_home(request):
    """dictionary with our dummy data as key to give access to home template"""
    context_key = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context_key)

"""Function presenting the blog about page"""
def blog_about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
