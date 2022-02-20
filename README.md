# Ecommerce


##  Tecnologias

Este projeto é feito em Django para criar uma aplicação para Ecommerce.

## Escopo do Projeto

- Projeto de Ecommerce constitui de varias aplicações que compõe uma loja.
  - Contas
  - Catalogo
    - Categorias
    - Produtos
  - Checkout
    - Order
    - Cart

# O que foi feito para desenvolver o projeto

- Primeiro passo foi aprender a forma como funciona a framework
- Depois você começa a definir o modelos para cada aplicação
- Define a relação entre esses modelos
- Você pode testa-los de forma rápida e simples pelo admin da framework
- Ou pode criar, editar e deletar pelo shell com o ORM
- Depois de criado os modelos você pode construir o templates, que vão renderizar a informações de forma personalizda.
- Neste momento você pode aplicar o HTML, CSS e JS para criar o frontend com a redenrização a partir do templates.
- Foram feitos alguns testes para testar os modelos e se as funcionalidades estão de acordo esperado
- É bom ir fazendo deploy da aplicação para ver se esta tudo correto...
- É bem chatinho fazer a configurações, mas quando esta tudo ok, e lindo de se ver...


## Primeiros Passos

1. Clone do  repositório
2. Entre na pasta do projeto
3. Crie um virtualenv com Python3
  ```
  $ python3 -m venv venv
  ```
4. Ative o virtualenv
   
  ```
  $ . venv/bin/activate
  ```
5. Instale as dependências

  ```
  $ pip install -r requirements.txt
  ```
   
6. Copie o ENV_SAMPLE para um novo arquivo chamado .env que será usado para
armazenar a informações sensivéis da aplicação

7. Execute as migrations
  ```
  $ ./manage.py makemigrations
  $ ./manage.py migrate
  ```
8. Execute a aplicação

  ```
  $ ./manage.py runserver
  ```

### Este projeto ainda esta em fase de construção
  - Adicionar um forma de manter a imagens na aplicação, a melhor solução vai ser usar um serviço a AWS
  - Adicionar o Endereço para Entregas
  - Melhorar a visual da aplicação
  - Organizar melhor o menus e adicionar um conteudo melhor na pagina inicial
  - Colocar alguma coisa com Vue JS... Talvez o carrinho e algum formulário...
