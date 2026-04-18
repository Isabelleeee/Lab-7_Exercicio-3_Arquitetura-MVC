# 📚 Livraria MVP - Arquitetura Multicamada

Este repositório contém a evolução do MVP de uma livraria virtual. O objetivo principal desta versão foi refatorar o sistema de um padrão MVC básico para uma **Arquitetura em Camadas (Layered Architecture)**, visando desacoplamento e facilidade de manutenção.

---

## 🏗️ Arquitetura do Projeto

O sistema foi dividido em **4 camadas principais**, respeitando a regra de que uma camada superior só pode se comunicar com a camada imediatamente abaixo:

1. **Presentation Layer (Interface/Web):** Rotas HTTP e front-end com **Flask** e **Jinja2**.
2. **Application Layer (Services):** Lógica de negócio, filtros e validações.
3. **Domain Layer (Entities):** Objetos de negócio e regras globais.
4. **Infrastructure Layer (Repository):** Simulação de banco de dados e persistência.

---

## ✨ Nova Feature: Controle de Estoque Inteligente

Nesta refatoração, foi implementada a funcionalidade de **Filtro Automático de Disponibilidade**:
* A camada de **Infraestrutura** armazena a quantidade em estoque.
* A camada de **Aplicação (Service)** garante que o catálogo exiba apenas itens com `estoque > 0`.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Framework Web:** Flask
* **Template Engine:** Jinja2
* **Versionamento:** Git

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
