#passo a passo de como criar um projeto django
# 1 - baixar a biblioteca
#verificar se esta instalado " django-admin --version "
# 2 - startar o programa python de djnago= comando: django-admin startproject nome_do_projeto
# 3 - entrar na pasta do projeto: cd nome_do_projeto
# 3 - para colocar no ar e rodar o servidor local: "python manage.py runserver"
# 4 - cd nome_do_projeto
# 5 - criar um app: "python manage.py startapp" nome_do_app

# componentes do django
# arqivos asgi e wsgi= para deploy
# urls= arquivo de rotas
# settings= arquivo de configurações
# manage= arquivo de gerenciamento do projeto

# componentes do app
# migrations= arquivo de migrações do banco de dados
# admin= arquivo de administração do app
# apps= arquivo de configuração do app
# tests= arquivo de testes do app   
# models= arquivo de modelos do app(criar as coisas que vão para o banco de dados)
# views= arquivo de views do app(criar a logica do app)[aqui que se cria as funções]- linkar backend com frontend
# db.sqlite3= arquivo do banco de dados(sqlite3 é o banco de dados padrão do django)[aqui que ficam os dados salvos do app]

# como login e cadastro e etc. obs: pode apagar esse arquivo que ele é recriado quando rodar o servidor(inclusive isso é melhor )


#apos criar os models tem que fazer as migrações(transformar os models em tabelas no banco de dados sqlite3)
#tem que estar na pasta do projeto com o manage.py
# 1 - python manage.py makemigrations    (serve para criar as migrações[as migracoes são as atualizações do banco de dados])
# 2 - python manage.py migrate    (serve para aplicar as migrações[as migracoes são as atualizações do banco de dados])

# painel do administrador do django
# 1 - criar um super usuário: python manage.py createsuperuser
# 2 - colocar um nome de usuário, email e senha
# 3 - rodar o servidor: python manage.py runserver
# 4 - entrar no painel do admin: localhost:8000/admin
#username=bernado_adm
#Email address: bccl@cesar.school
#pass=adm123
#como adicionar o app no painel do admin
# 1 - entrar no arquivo admin.py do app
# 2 - importar o model do app: from .models import NomeDoModel
# 3 - registrar o model: admin.site.register(NomeDoModel)
# 4 - entrar no painel do admin: localhost:8000/admin

# html
#quando vc abre % % esta chamando uma função do djangono html 
#exemplo: {% block content %}  {% endblock content %}(serve para delimitar uma seção de conteúdo que pode ser substituída por outras páginas que estendem esse template base)
# {% extends pasta dentro de templates/ o arquivo que tu quer tirar o bloco %}