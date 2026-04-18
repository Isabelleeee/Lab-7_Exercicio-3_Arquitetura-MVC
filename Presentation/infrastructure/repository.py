from domain.models import Livro

class LivroRepository:
    def __init__(self):
        # Simulação de banco de dados
        self.dados = [
            Livro(1, "O Alquimista", "Paulo Coelho", 45.0, 10),
            Livro(2, "1984", "George Orwell", 39.9, 0) # Esgotado
        ]

    def listar_todos(self):
        return self.dados