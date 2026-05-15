from django import forms
from django.contrib.auth.models import User

from .models import Mensaje


class MensajeForm(forms.ModelForm):
    receptor = forms.ModelChoiceField(
        queryset=User.objects.none(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Para",
    )

    class Meta:
        model = Mensaje
        fields = ("receptor", "contenido")
        widgets = {
            "contenido": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }

    def __init__(self, *args, usuario=None, **kwargs):
        super().__init__(*args, **kwargs)
        queryset = User.objects.all()
        if usuario and usuario.is_authenticated:
            queryset = queryset.exclude(pk=usuario.pk)
        self.fields["receptor"].queryset = queryset.order_by("username")
