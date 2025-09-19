from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout

# Create your views here.
def logout_view(request):
    logout(request) # Função para fazer logout do usuário
    return HttpResponseRedirect(reverse('index')) # Redireciona para a página inicial após logout
