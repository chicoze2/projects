from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



from .models import *
from .forms import *

def home_view(request):    
    
    if request.user.is_authenticated:

      if request.user.is_staff:
        protocolos = Protocolo.objects.all().order_by('-pk') ## Do maior  ID pro menor
      else:
        protocolos = Protocolo.objects.filter(empresa=request.user. empresa).order_by('-pk')


      ctx = {'protocolos': protocolos}
      return render(request, 'home.html', ctx)

    else:
      return redirect('login_url')


###################
## USER FUNCIONS ##
###################

def login_view(request):
  
  page = 'login'

  if request.user.is_authenticated:
    return redirect('/')

  if request.method == 'POST':
    username = request.POST.get('username').lower()
    password = request.POST.get('password')

    try:
      user = User.objects.get(username=username)
    except:
      messages.error(request, "User does not exist")

    user = authenticate(request, username=username, password=password) 

    if user is not None:
      login(request, user)
      return redirect('/')
    else:
      messages.error(request, "Username or password is incorrect")

  context = {'page': page}
  return render(request, 'forms/login_register.html', context)

@login_required(login_url='login')
def logout_function(request):
  print('>>>>> logout function')
  logout(request)
  return redirect('/')  

def create_new_user_view(request):
  page = 'register'
  form = CustomUserCreationForm()

  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)

      user.username = user.username.lower() 
      user.save()
      login(request, user)
      return redirect('/')
    else:
      messages.error(request,'Something went wrong. Please try again')

  context = {'page': page, 'form': form}
  return render(request, 'forms/login_register.html', context)

@login_required(login_url='login')
def update_user_view(request):

  user = request.user
  form = SimpleUserEditForm(instance=user) 

  if user.is_staff:
    form = AdvancedUserEditForm(instance=user) 

  if request.method == 'POST':
    
    SimpleUserEditForm(request.POST, request.FILES, instance=user)
    if request.user.is_staff:
      form = AdvancedUserEditForm(request.POST, request.FILES, instance=user)


    if form.is_valid():
      form.save()
      print('>>>>>>>> form saved successfully')
      return redirect('/', user.id)

  return render(request, 'forms/update_user_form.html', {"form": form})

#####################
#### PROTOCOLOS #####
#####################
def create_protocol_view(request):

    if not request.user.empresa:
      messages.error(request, 'Usuário não pertence a empresa.')
      
    form = CreateProtocolForm()
    if request.method == 'POST':


        form = CreateProtocolForm(request.POST, initial={"empresa": request.user.empresa, "author": request.user})
        protocolo = form.save(commit=False) ## objeto protocolo vindo do form
        protocolo.author = request.user
        protocolo.empresa = request.user.empresa

        if form.is_valid():
            form.save()
            return redirect('/')

        else:
          print(form.errors)
          messages.error(request, 'Informações inconsistentes. Erro ao criar protocolo.')

    ctx = {'form': form}
    return render(request, 'forms/create_protocol_form.html',ctx)

def edit_protocol_view(request, pk):
  
  form = EditProtocolForm(request.POST)

  ctx = {'form': form}
  return render(request, 'forms/edit_protocol_form.html', ctx)