#coding: utf-8
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,reverse,redirect
from django.views.generic import TemplateView, ListView, DetailView, View
from .models import Blog

# Create your views here.

class IndexView(TemplateView):
    template_name = 'blog/index.html'



def add(request):

    if request.method == 'GET':

        return render(request,'blog/add.html')

    elif request.method == 'POST':

        #获取表单内容

        title = request.POST.get('title')

        content = request.POST.get('content')

        #添加到数据库中

        Blog.objects.create(title=title,content=content)

        return HttpResponse('发布成功')

    else:

        return HttpResponse('这是不能处理的操作')


def list(request):

    blogs = Blog.objects.all()
    return render(request,'blog/list.html',{'blogs':blogs})

def detail(request,blog_id=0):

    blog = Blog.objects.get(id=blog_id)

    return render(request,'blog/detail.html',{'blog':blog})

def delete(request,blog_id=0):

    blog = Blog.objects.get(id=blog_id)

    if blog:

        blog.delete()

        return redirect(reverse('blog_list'))

    else:

        return HttpResponse('要删除的数据不存在')

def modify(request,blog_id=0):

    blog = Blog.objects.get(id=blog_id)

    if blog:

        if request.method == 'GET':

            return render(request, 'blog/edit.html', context={'blog': blog})

        elif request.method == 'POST':

            title = request.POST.get('title')

            content = request.POST.get('content')

            blog.title = title

            blog.content = content

            blog.save()

            return HttpResponse('修改成功')

        else:

            return HttpResponse('该操作无法执行')

    else:

        return HttpResponse('数据不存在')