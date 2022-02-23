from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Blog
from .forms import BlogForm


def blog(request):
    """ A view to show all blog posts """

    blog = Blog.objects.all()

    context = {
        'blog.blog': blog,
    }

    return render(request, 'blog/blog.html', context)


    