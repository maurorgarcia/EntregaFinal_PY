from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import MensajeForm
from .models import Mensaje


@login_required
def inbox(request):
    # Inbox: mensajes recibidos por el usuario logueado.
    mensajes = Mensaje.objects.filter(receptor=request.user)
    return render(request, "messenger/inbox.html", {"mensajes": mensajes})


@login_required
def sent(request):
    # Enviados: mensajes que el usuario logueado mandó a otros usuarios.
    mensajes = Mensaje.objects.filter(emisor=request.user)
    return render(request, "messenger/sent.html", {"mensajes": mensajes})


@login_required
def compose(request):
    # Compose: crear un mensaje. El emisor se setea con request.user.
    if request.method == "POST":
        form = MensajeForm(request.POST, usuario=request.user)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.emisor = request.user
            mensaje.save()
            messages.success(request, "Mensaje enviado.")
            return redirect("messenger:sent")
    else:
        form = MensajeForm(usuario=request.user)

    return render(request, "messenger/compose.html", {"form": form})
