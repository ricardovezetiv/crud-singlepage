from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import ClientForm
from .models import Client


def dashboard(request):
    if request.method == "POST":
        form = ClientForm(request.POST or None)
        if form.is_valid():
            form.save()
            clients = Client.objects.all()
            messages.success(request, "Client has been added!")
            return render(request, "crud/dashboard.html", {"clients": clients})
    else:
        clients = Client.objects.all()
        return render(request, "crud/dashboard.html", {"clients": clients})


def edit(request, client_id):
    if request.method == "POST":
        client = Client.objects.get(id=client_id)
        form = ClientForm(request.POST or None, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, "Client has been edited!")
            return redirect("/")
    else:
        client = Client.objects.get(id=client_id)
        clients = Client.objects.all()
        return render(
            request,
            "crud/dashboard.html",
            {"client": client, "clients": clients},
        )


def delete(request, client_id):
    client = Client.objects.get(id=client_id)
    client.delete()
    messages.success(request, "Client has been Deleted!")
    return redirect("/")
