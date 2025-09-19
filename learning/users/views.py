from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout,login,authenticate
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request):
    logout(request) # Função para fazer logout do usuário
    return HttpResponseRedirect(reverse('index')) # Redireciona para a página inicial após logout

def register(request):
    """registra um novo usuario"""
    if request.method !='POST':
        #exibe o formulario em branco
        form = UserCreationForm()
    else:
        #processa o form prenechido
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()#salva o novo usuario
            #faz login do novo usuario e redireciona para a página inicial
            authenticated_user = authenticate(user=new_user.username,password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('index'))
    context = {'form':form}
    return render(request,'users/register.html',context)
            
    
