from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["receiver", "content"]
        labels = {
            "receiver": "Destinatario",
            "content": "Mensaje",
        }
        widgets = {
            "content": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        if self.user:
            self.fields["receiver"].queryset = self.fields["receiver"].queryset.exclude(
                pk=self.user.pk
            )

    def clean_receiver(self):
        receiver = self.cleaned_data["receiver"]

        if self.user and receiver == self.user:
            raise forms.ValidationError("No podés enviarte un mensaje a vos mismo.")

        return receiver