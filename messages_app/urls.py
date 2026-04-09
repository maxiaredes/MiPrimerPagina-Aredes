from django.urls import path
from . import views

app_name = "messages_app"

urlpatterns = [
    path("", views.inbox, name="inbox"),
    path("enviar/", views.send_message, name="send_message"),
    path("<int:pk>/", views.message_detail, name="message_detail"),
    path("enviados/", views.sent_messages, name="sent_messages"),
]