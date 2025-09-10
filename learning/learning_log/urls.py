from django.urls import path  # não vai ser usado o include
from learning_log import views

urlpatterns = [
    path('', views.index, name='index'),  # joga para a view index
    path('topics/', views.topics, name='topics'),  # lista todos os tópicos
    path('topicos/<int:topico_id>/', views.topicos, name='topicos'),
    # mostra um tópico específico com base no ID passado na URL
    path('new_topic', views.new_topic, name='new_topic'),  # página para adicionar um novo tópico
    path('new_entry/<int:topic_id>/',view=views.new_entry,name='new_entry'),#página para adicionar uma nova entrada e associa-la a um tópico específico com base no ID do tópico passado na URL
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),  # página para editar uma entrada específica com base no ID da entrada passado na URL
]

# o <int:topico_id> indica que a url vai receber um número inteiro que será passado para a view topicos como parâmetro  