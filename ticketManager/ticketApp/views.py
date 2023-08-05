from django.shortcuts import render

from .models import Protocolo

from .forms import CreateProtocolForm

def home_view(request):    
    protocolos = Protocolo.objects.all()

    ctx = {'protocolos': protocolos}
    return render(request, 'home.html', ctx)

def create_protocol_view(request):

    form = CreateProtocolForm()
    if request.method == 'POST':
        form = CreateProtocolForm(request.POST)

        if form.is_valid():
            protocolo = form.save(commit=False) ## objeto protocolo vindo do form
            # protocolo.author =- request.user TODO AFTER LOGIN FUNCIOTNM

            form.save()

    ctx = {'form': form}
    return render(request, 'forms/create_protocol_form.html',ctx)

# def ## TODO USER FUNCIOTN