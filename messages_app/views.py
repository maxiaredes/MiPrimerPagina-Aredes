from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm


@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user).order_by("-created_at")
    return render(request, "messages_app/inbox.html", {"messages": messages})


@login_required
def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST, user=request.user)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect("messages_app:inbox")
    else:
        form = MessageForm(user=request.user)

    return render(request, "messages_app/send_message.html", {"form": form})


@login_required
def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk, receiver=request.user)
    return render(request, "messages_app/message_detail.html", {"message": message})

@login_required
def sent_messages(request):
    messages = Message.objects.filter(sender=request.user).order_by("-created_at")
    return render(
        request,
        "messages_app/sent_messages.html",
        {"messages": messages},
    )