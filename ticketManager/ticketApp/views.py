from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required




from .models import *
from .forms import *

def home_view(request):    
    
    if request.user.is_authenticated:

      if request.user.is_staff:
        protocolos = Protocolo.objects.all().order_by('-pk') ## Do maior  ID pro menor
      else:
        protocolos = Protocolo.objects.filter(empresa=request.user.empresa).order_by('-pk')


      ctx = {'protocolos': protocolos, 'page': 'home'}
      return render(request, 'home.html', ctx)

    else:
      return redirect('login_url')

@permission_required('is_staff')
def supervisor_view(request):

  empresas = Empresa.objects.all()
  protocolos = Protocolo.objects.all()
  users = User.objects.all()

  q = request.GET.get('q')
  page = ''
  listagem = ''

  if q =='users':
    listagem = {
      'title' : 'Usuarios',
      'col1' : 'ID',
      'col2' : 'Nome',
      'col3':  'Email',
      'col4':  'Empresa'
      
    }
    page = 'users'
    

  elif q == 'empresas':

    listagem = {
      'title' : 'Empresas',
      'col1' : 'ID',
      'col2' : 'Nome',
      'col3':  'Protocolos',
      'col4':  'Usuarios'
      
    }
    page = 'empresas'

  elif q == 'protocolos':
    listagem = {
      'title' : 'Protocolos',
      'col1' : 'ID',
      'col2' : 'Nome',
      'col3':  'Descricao',
      'col4':  'Empresa',
      'col5': 'Data'
    }
    page = 'protocolos'
    
  elif not q:

    listagem = {
      'title' : 'Empresas',
      'col1' : 'ID',
      'col2' : 'Nome',
      'col3':  'Protocolos',
      'col4':  'Usuarios'
      
    }
    page = 'empresas'


  context = {'empresas': empresas, 'users': users, 'protocolos': protocolos, 'page': page, 'listagem': listagem}
  return render(request, 'supervisor.html', context)

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
      print('--------------')
      user = form.save(commit=False)

      user.username = user.username.lower() 
      user.save()
      login(request, user)
      return redirect('/')
    else:
      print(form.errors)
      messages.error(request, form.errors)

  context = {'page': page, 'form': form}
  return render(request, 'forms/login_register.html', context)

@login_required(login_url='login')
def update_user_view(request, user_id=None):

  if user_id == None:
    user_id = request.user.id

  user = get_object_or_404(User, pk=user_id)
  

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
    else:
      print('>>>>>>>>>> err')

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
  
  protocol = Protocolo.objects.get(id = int(pk))
  data = {'name': protocol.name, 'description': protocol.description}
  form = EditProtocolForm(data)

  ctx = {'form': form}
  return render(request, 'forms/edit_protocol_form.html', ctx)

def list_by_empresa_view(request):
  empresa_id = request.GET.get('selected_empresa')
  empresa_nome = Empresa.objects.get(id=empresa_id)
  protocolos = Protocolo.objects.filter(empresa__id=empresa_id)
  
  ctx = {'protocolos': protocolos, 'empresa': empresa_nome}
  return render(request, 'list_by_empresa.html', ctx)


@permission_required('is_staff')
def create_empresa_view(request):

  return render(request, 'forms/create_empresa.html')