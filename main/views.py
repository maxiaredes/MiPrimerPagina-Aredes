from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserEditForm, ProfileEditForm
from .models import Profile


def home(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")


def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()

    return render(request, "main/signup.html", {"form": form})


@login_required
def perfil(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, "main/perfil.html", {"profile": profile})


@login_required
def editar_perfil(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("main:perfil")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=profile)

    return render(
        request,
        "main/editar_perfil.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
        },
    )