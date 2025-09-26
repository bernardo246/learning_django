from django.shortcuts import render
from .models import Topic, Entry  # importar o model Topic para usar na view topics
from .forms import TopicForm, EntryForm  # importar o formulário TopicForm para usar na view new_topic
from django.http import HttpResponseRedirect# importa HttpResponseRedirect para redirecionar após o formulário ser salvo
from django.urls import reverse# importa o reverse para usar na view new_topic
from django.contrib.auth.decorators import login_required# importa o decorator login_required para proteger as views que precisam de login
from django.http import Http404

# Create your views here.
def index(request):
    """The home page for Learning Log."""
    # renderiza o arquivo index.html que está na pasta templates
    # (a função render recebe 3 parâmetros: request, nome do arquivo html, dicionário com dados para passar para o html)
    return render(request, 'learning_log/index.html')

@login_required
def topics(request):
    """Mostra todos os tópicos."""
    topic = Topic.objects.filter(ower=request.user).rder_by('date_added')  # pega todos os tópicos do banco de dados e ordena pela data de adição
    context = {'topics': topic}  # cria um dicionário com os tópicos
    # renderiza o arquivo topics.html e passa o dicionário context para o html
    return render(request, 'learning_log/topics.html', context)

@login_required
def topicos(request, topico_id):
    """"Mostra um assunto e todas as entradas associadas a ele"""
    topic = Topic.objects.get(id=topico_id)  # pega o tópico com o id igual ao topico_id passado na url
    # pega todas as entradas associadas ao tópico e ordena pela data de adição
    # (o "-" antes do date_added indica que a ordem é decrescente)
    # garante que o assunto pertence ao usuario atual
    if topic.ower != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')# entry_set é um gerenciador de relacionamento reverso que permite acessar as entradas associadas a um tópico
    context = {'topic': topic, 'entries': entries}  # cria um dicionário com o tópico e as entradas
    # renderiza o arquivo topico.html e passa o dicionário context para o html
    return render(request, 'learning_log/topico.html', context)
@login_required
def new_topic(request):
    """Adiciona um novo tópico"""
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco.
        form = TopicForm()# cria um formulário em branco
    else:
        # Dados submetidos; processa os dados.
        form = TopicForm(request.POST)# cria um formulário com os dados submetidos
        if form.is_valid():# verifica se o formulário é válido
            new_topic =form.save(commit=False)# salva o formulário 
            new_topic.owner= request.user
            new_topic.save()# salva o formulário no banco de dados
            return HttpResponseRedirect(reverse('topics'))# redireciona para a página de tópicos(o reverse pega o nome da url e devolve a url correspondente)

    # Exibe um formulário em branco ou inválido.
    context = {'form': form}# cria um dicionário com o formulário
    return render(request, 'learning_log/new_topico.html', context)# renderiza o arquivo new_topic.html e passa o dicionário context para o html

@login_required
def new_entry(request, topic_id):
    """Adiciona uma nova entrada para um assunto em particular."""
    topic = Topic.objects.get(id=topic_id)  # pega o tópico com o id == topic_id passado na url
        # garante que o assunto pertence ao usuario atual
    if topic.ower != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm()  # cria um formulário em branco
    else:
        form = EntryForm(data=request.POST)  # cria um formulário com os dados submetidos
        if form.is_valid():  # verifica se o formulário é válido
            new_entry = form.save(commit=False)  # cria um novo objeto Entry, mas não salva ainda
            new_entry.topic = topic  # associa a nova entrada ao tópico correto
            new_entry.save()  # salva a nova entrada no banco de dados
            return HttpResponseRedirect(reverse('topicos', args=[topic_id]))  # redireciona para a página do tópico correto

    context = {'topicos': topic, 'form': form}  # cria um dicionário com o tópico e o formulário
    return render(request, 'learning_log/new_entry.html', context)
@login_required
def edit_entry(request, entry_id):
    """edita uma entrada existente"""
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic# pega o tópico associado a entrada
        # garante que o assunto pertence ao usuario atual
    if topic.ower != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance=entry)# forma preenchida com a entrada existente
    else:
        form = EntryForm(instance=entry,data=request.POST)# formulário preenchido com os dados submetidos(o instance=entry garante que estamos editando a entrada existente)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topicos',args=[topic.id]))# redireciona para a página do tópico correto'))
    context = {'entry': entry, 'topic': topic, 'form': form}  # cria um dicionário com a entrada, o tópico e o formulário
    return render(request, 'learning_log/edit_entry.html',context)

