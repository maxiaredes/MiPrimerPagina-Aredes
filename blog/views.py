from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    busqueda = request.GET.get("busqueda", "")

    if busqueda:
        posts = posts.filter(titulo__icontains=busqueda)

    return render(request, "blog/post_list.html", {
        "posts": posts,
        "search_query": busqueda,
    })


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect("blog:post_list")
    else:
        form = PostForm()

    return render(request, "blog/post_create.html", {"form": form})

from django.db.models import Q

def post_list(request):
    busqueda = request.GET.get("busqueda", "")
    posts = Post.objects.all()

    if busqueda:
        posts = posts.filter(
            Q(titulo__icontains=busqueda) | Q(contenido__icontains=busqueda)
        )

    return render(request, "blog/post_list.html", {
        "posts": posts,
        "search_query": busqueda,
    })