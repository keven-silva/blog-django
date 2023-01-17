# blog-django
Blog desenvolvido com o framework django, boostrap e sqlite3. O blog possui acesso a uma tela ``admin``, onde se é possivel cadastrar categorias, usuários e novos posts.

## Funcionalidades
- Cadastro de usuário
- Cadastro de categorias
- Cadastro de posts
- Cadastro de comentários
- Filtro de posts
- Mensagem de validação
- Testes unitários

## Execução do código
    python manage.py makemigrations
  
### Exporta as migrations para o banco de dados
    python manage.py migrate

### Criar super usuário
    python manage.py createsuperuser

### Subir no servidor local
    python manage.py runserver
