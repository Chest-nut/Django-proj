# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from . import models


def index(request):
    blogs = models.Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})

def edit(request, blog_id):
    if blog_id is '0':
        return render(request, 'edit.html')
    blog = models.Blog.objects.get(pk=blog_id)
    return render(request, 'edit.html', {'blog': blog})

def detail(request, blog_id):
    blog = models.Blog.objects.get(pk=blog_id)
    return render(request, 'detail.html', {'blog': blog})

def edit_action(request):
    title = request.POST.get('title', 'Title')
    content = request.POST.get('content', 'Content')
    blog_id = request.POST.get('blog_id')
    if blog_id is '0':
        models.Blog.objects.create(title=title, content=content)
        blogs = models.Blog.objects.all()
        return render(request, 'index.html', {'blogs': blogs})

    blog = models.Blog.objects.get(pk=blog_id)
    blog.title = title
    blog.content = content
    blog.save()
    return render(request, 'detail.html',  {'blog': blog})