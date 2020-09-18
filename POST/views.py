from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import post

# Create your views here.
# post.objects.order_by('id')[0:2]

def Home(request):
    q = request.GET.get('q', None)
    items = ''
    if q is None or q is "":
        # posts = post.objects.order_by('-pub_date')[0:2]
        posts = post.objects.order_by('-pub_date')
        # posts = post.objects.all()
    elif q is not None:
        posts = post.objects.filter(title__contains=q)
    context = {'posts': posts}
    return render(request, 'index.html', context)

def next(request):
    posts = post.objects.order_by('-pub_date')[2:4]
    context = {'posts': posts}
    return render(request, 'index.html', context)


def Add_post(request):
    if request.method == 'POST':
        # posts = post.objects.all()
        image = request.FILES["image"]
        title = request.POST["title"]
        body = request.POST["body"]
        author = request.POST["author"]
        post.objeccts.all()
        # print(Blog.objects.all())
        posts = post.objects.create(title = title, body = body, author = author,image = image)
        posts.save()
        return redirect('Home')
    else:
        return render(request,'Blog/add_post.html')



def detail(request, slug=None):
    posts = get_object_or_404(post, slug=slug)
    context = {'posts': posts}
    return render(request, 'Blog/detail.html', context)
