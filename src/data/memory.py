#armazena as análises feitas nos arquivos knowledge_base e pdf_parser
#armazena e recupera requisitos que ja foram analisados permitindo que o sistema aprenda com interações anteriores com o usuario
#é a memória de experiências do ReAct

class Memory:
    class Memory:
        def __init__(self, file_path="memory.json"):
            self.file_path = file_path
            self._load()

    def _load(self):
        try:
            with open(self.file_path, 'r') as f:
                self.past_requisicoes = json.load(f)
        except FileNotFoundError:
            self.past_requisicoes = {}

    def _save(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.past_requisicoes, f)

    def store(self, requisito, pontos_funcao):
        super().store(requisito, pontos_funcao)
        self._save() 

    def __init__(self):
        self.past_requisicoes = {}

    def store(self, requisito, pontos_funcao):
        # Armazena o requisito e a pontuação de função
        self.past_requisicoes[requisito] = pontos_funcao

    def retrieve(self, requisito):
        # Recupera a pontuação de função passada, se existir
        return self.past_requisicoes.get(requisito, None)
