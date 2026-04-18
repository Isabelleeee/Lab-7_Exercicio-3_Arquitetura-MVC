📚 Livraria MVP - Arquitetura Multicamada
Este repositório contém a evolução do MVP de uma livraria virtual. O objetivo principal desta versão foi refatorar o sistema de um padrão MVC básico para uma Arquitetura em Camadas (Layered Architecture), visando desacoplamento e facilidade de manutenção.

🏗️ Arquitetura do Projeto
O sistema foi dividido em 4 camadas principais, respeitando a regra de que uma camada superior só pode se comunicar com a camada imediatamente abaixo:

Presentation Layer (Interface/Web): Responsável por receber as requisições HTTP e renderizar o front-end utilizando Flask e Jinja2.

Application Layer (Services): Contém a lógica de negócio da aplicação. É aqui que as regras de filtragem e validações ocorrem antes de chegar ao usuário.

Domain Layer (Entities): Define os objetos de negócio (Entidades). É a camada mais estável e central do sistema.

Infrastructure Layer (Repository): Responsável pela persistência de dados. Nesta versão, simula um banco de dados em memória para fins de MVP.

✨ Nova Feature: Controle de Estoque Inteligente
Nesta refatoração, foi implementada a funcionalidade de Filtro Automático de Disponibilidade:

A camada de Infraestrutura agora armazena a quantidade em estoque de cada livro.

A camada de Aplicação (Service) filtra os livros, garantindo que o catálogo exibido na Interface mostre apenas itens com estoque > 0.

Isso garante que o usuário final nunca tente comprar um item indisponível.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.x

Framework Web: Flask

Template Engine: Jinja2

Versionamento: Git

🚀 Como Executar o Projeto
Clone o repositório:

Bash
git clone https://github.com/seu-usuario/seu-repositorio.git
Crie e ative um ambiente virtual (recomendado):

Bash
python -m venv venv
# No Windows:
.\venv\Scripts\activate
Instale as dependências:

Bash
pip install flask
Execute a aplicação:

Bash
python app.py
Acesse no navegador:
http://127.0.0.1:5000

📂 Estrutura de Pastas
Plaintext
├── app.py                  # Entry point (Presentation)
├── domain/
│   └── models.py           # Entidades de Negócio
├── services/
│   └── livro_service.py    # Lógica de Aplicação
├── infrastructure/
│   └── repository.py       # Persistência de Dados
├── templates/
│   └── index.html          # View (Front-end)
└── static/
    └── style.css           # Estilização
