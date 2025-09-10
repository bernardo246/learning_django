from django.contrib.auth.models import User

# lista todos os usuários
print(User.objects.all())

# pega o superusuário específico
u = User.objects.get(username="admin")   # troque "admin" pelo seu nome de usuário
print(u.username, u.email, u.is_superuser, u.is_staff)
