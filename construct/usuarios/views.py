from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from rolepermissions.decorators import has_permission_decorator
from .models import Users
from django.urls import reverse
from django.contrib import auth

# Create your views here.

@has_permission_decorator('cadastrar_vendedor')
def cadastrar_vendedor(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Users.objects.filter(email=email)

        if user.exists():
            # TODO: Utilizar messages do django
            return HttpResponse('Já existe o usuário')
        user = Users.objects.create_user(username=email, email=email, password=password, cargo="V")
        # TODO: Utilizar messages do django para redirecionar com uma mensagem
        return HttpResponse('Conta do usuário criada')
    else:
        vendedores = Users.objects.filter(cargo="V")
        return render(request,'cadastrar_vendedor.html', {'vendedores':vendedores})

@has_permission_decorator('cadastrar_vendedor')
def excluir_usuario(request, id):
    vendedor = get_object_or_404(Users, id=id)
    vendedor.delete()
    return redirect(reverse('cadastrar_vendedor'))

def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse('plataforma'))
        return render(request,'login.html')
    elif request.method =="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(username=email, password=password)

        if not user:
            #TODO: Redirecionar com mensagem de erro
            return HttpResponse('Usuário inválido!')
        else:
            auth.login(request,user)
            return HttpResponse('Usuário logado com sucesso')

def logout(request):
    request.session.flush()
    return redirect(reverse('login'))
