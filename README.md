# 📚 Livraria MVP - Arquitetura Multicamada

Este repositório contém a evolução do MVP de uma livraria virtual. O objetivo principal desta versão foi refatorar o sistema de um padrão MVC básico para uma **Arquitetura em Camadas (Layered Architecture)**, visando um maior desacoplamento, organização estrutural e facilidade de manutenção.

---

## 🏗️ Arquitetura do Projeto

O sistema foi dividido em **4 camadas principais**, respeitando rigorosamente a regra de que uma camada superior só pode se comunicar com a camada imediatamente abaixo:

1. **Presentation Layer (Interface/Web):** Responsável por receber as requisições HTTP e renderizar o front-end utilizando **Flask** e **Jinja2**.
2. **Application Layer (Services):** Contém a lógica de aplicação e regras de negócio específicas desta versão. Faz a ponte entre a interface e o domínio.
3. **Domain Layer (Entities):** Define os objetos de negócio centrais (Entidades). É a camada mais estável e central do sistema.
4. **Infrastructure Layer (Repository):** Responsável pela persistência de dados. Nesta versão, atua simulando um banco de dados em memória.

---

## ✨ Nova Feature: Controle de Estoque Inteligente

Nesta refatoração, foi implementada a funcionalidade de **Filtro Automático de Disponibilidade**:
* A camada de **Infraestrutura** agora armazena a quantidade em estoque de cada livro.
* A camada de **Aplicação (Service)** aplica uma regra de negócio que filtra os livros, garantindo que o catálogo exibido na **Interface** mostre apenas itens com `estoque > 0`.
* Isso impede que itens esgotados sejam apresentados ao usuário final.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Framework Web:** Flask
* **Front-end:** HTML5 + CSS3 + Jinja2
* **Versionamento:** Git

---

## 📂 Estrutura de Pastas

```text
├── app.py                  # Entry point / Presentation
├── domain/
│   └── models.py           # Entidades de Negócio (Camada 3)
├── services/
│   └── livro_service.py    # Lógica de Aplicação (Camada 2)
├── infrastructure/
│   └── repository.py       # Persistência de Dados (Camada 4)
├── templates/
│   └── index.html          # View (Front-end)
└── static/
    └── style.css           # Estilização
```

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
   ```

2. **Instale as dependências:**
   Certifique-se de ter o Python instalado e rode o comando:
   ```bash
   pip install flask
   ```

3. **Inicie a aplicação:**
   No terminal, dentro da pasta principal do projeto, execute:
   ```bash
   python app.py
   ```

4. **Acesse no navegador:**
   Abra a URL `http://127.0.0.1:5000` para testar o MVP.
