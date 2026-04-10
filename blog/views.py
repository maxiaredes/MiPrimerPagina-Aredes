from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        busqueda = self.request.GET.get("busqueda", "")

        if self.request.user.is_staff:
            queryset = Post.objects.exclude(estado="ARCHIVADO")
        else:
            queryset = Post.objects.filter(estado="PUBLICADO")

        if busqueda:
            queryset = queryset.filter(
                Q(titulo__icontains=busqueda) |
                Q(subtitulo__icontains=busqueda) |
                Q(contenido__icontains=busqueda)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("busqueda", "")

        cantidad = len(context["posts"])
        resto = cantidad % 3

        if cantidad == 0:
            context["placeholders"] = 0
        elif resto == 0:
            context["placeholders"] = 0
        else:
            context["placeholders"] = 3 - resto

        return context

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["titulo", "subtitulo", "contenido", "imagen", "estado"]
    success_url = reverse_lazy("blog:post_list")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["titulo", "subtitulo", "contenido", "imagen", "estado"]
    success_url = reverse_lazy("blog:post_list")

    def test_func(self):
        return self.request.user.is_staff


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post_list")

    def test_func(self):
        return self.request.user.is_staff