from django.shortcuts import render, redirect
from django.views import View
from .models import Client
from .forms import ClientForm

class ClientList(View):
    def get(self, request):
        clients = Client.objects.all()
        return render(request, 'clients/client_list.html', {'clients': clients})

class ClientDetail(View):
    def get(self, request, id):
        client = Client.objects.get(id=id)
        return render(request, 'clients/client_detail.html', {'client': client})

class ClientCreate(View):
    def get(self, request):
        form = ClientForm()
        return render(request, 'clients/new.html', {'form': form})

    def post(self, request):
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
        return render(request, 'clients/new.html', {'form': form})

class ClientUpdate(View):
    def get(self, request, id):
        client = Client.objects.get(id=id)
        form = ClientForm(instance=client)
        return render(request, 'clients/update.html', {'form': form})

    def post(self, request, id):
        client = Client.objects.get(id=id)
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
        return render(request, 'clients/update.html', {'form': form})

class ClientDelete(View):
    def get(self, request, id):
        client = Client.objects.get(id=id)
        client.delete()
        return redirect('client_list')