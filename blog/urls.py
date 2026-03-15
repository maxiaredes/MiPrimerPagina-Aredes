from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="post_list"),   # lista de posts
    path("crear/", views.post_create, name="post_create"),   # crear post
]