from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["titulo", "contenido", "imagen", "estado", "autor"]
    success_url = reverse_lazy("blog:post_list")


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["titulo", "contenido", "imagen", "estado", "autor"]
    success_url = reverse_lazy("blog:post_list")


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post_list")