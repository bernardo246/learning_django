from django.db import models
#manipulacao do banco de dados
# Create your models here.
from django.contrib.auth.models import User

#isso vai ser usado para criar as tabelas no banco de dados
class Topic(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo"""
    text = models.CharField(max_length=200,unique=True) #campo de texto com tamanho máximo de 200 caracteres
    date_added = models.DateTimeField(auto_now_add=True) #campo de data e hora que é adicionado automaticamente quando o objeto é criado
    ower= models.ForeignKey(User,on_delete=models.CASCADE)#chave estrangeira que liga a tabela Topic com a tabela User do django
    #o on_delete=models.CASCADE faz com que quando o usuário for deletado, todos os tópicos associados a ele também sejam deletados

    def __str__(self):# esse comando faz com que o django devolva o texto do modelo quando for chamado
        """devolve uma representação em string do modelo"""
        return self.text

class Entry(models.Model):
    """algo específico que o usuário aprendeu sobre um assunto"""
    topic= models.ForeignKey(Topic, on_delete=models.CASCADE)#chave estrangeira que liga a tabela Entry com a tabela Topic
    text=models.TextField()#campo de texto sem limite de caracteres
    date_added=models.DateTimeField(auto_now_add=True)#campo de data e hora que é adicionado automaticamente quando o objeto é criado

    class Meta:
        verbose_name_plural='entries'#esse comando faz com que o django use o nome entries no plural ao invés de entrys
    def __str__(self):#questao de organização
        """devolve uma representação em string do modelo"""
        return self.text[:50] + "..." 
