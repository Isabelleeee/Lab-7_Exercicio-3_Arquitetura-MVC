class LivroService:
    def __init__(self, repository):
        self.repo = repository

    def obter_catalogo_disponivel(self):
        # Regra de negócio: só mostra o que tem no estoque
        todos = self.repo.listar_todos()
        return [l for l in todos if l.estoque > 0]