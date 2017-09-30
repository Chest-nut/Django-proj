# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render

from . import models


def index(request):
    """首页"""

    blogs = models.Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})


def edit(request, blog_id):
    """编辑页面"""

    # 添加新文章时，blog_id为0
    if blog_id is '0':
        return render(request, 'edit.html')
    # blog_id不为0时，进入文章修改页面
    else:
        blog = models.Blog.objects.get(pk=blog_id)
        return render(request, 'edit.html', {'blog': blog})


def detail(request, blog_id):
    """博客文章详情页面"""

    blog = models.Blog.objects.get(pk=blog_id)
    return render(request, 'detail.html', {'blog': blog})


def edit_action(request):
    """表单请求处理函数"""

    title = request.POST.get('title', 'Title')
    content = request.POST.get('content', 'Content')
    blog_id = request.POST.get('blog_id')

    # 请求添加新文章时，向数据库插入记录，然后跳转到首页
    if blog_id is '0':
        models.Blog.objects.create(title=title, content=content)
        blogs = models.Blog.objects.all()
        return render(request, 'index.html', {'blogs': blogs})
    # 请求修改文章时，修改数据库记录，然后跳转到文章详情页面
    else:
        blog = models.Blog.objects.get(pk=blog_id)
        blog.title = title
        blog.content = content
        blog.save()
        return render(request, 'detail.html',  {'blog': blog})