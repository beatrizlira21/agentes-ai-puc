from src.data.knowledge_base import KnowledgeBase
from src.domain.usecases import AnalisarPontoFuncao
from src.data.memory import Memory  # Importa a nova classe Memory

class CLI:
    def __init__(self, pdf_path):
        self.memory = Memory()  # Instancia a memória
        self.knowledge_base = KnowledgeBase(pdf_path)
        self.analisador = AnalisarPontoFuncao(self.knowledge_base, self.memory)

    def iniciar(self):
        print("🔄 Carregando regras do PDF...")
        print("✅ Regras com sucesso!")
        #print(self.knowledge_base.get_regras())

        while True:
            requisito = input("Digite o requisito (ou 'sair' para encerrar): ")
            if requisito.lower() == 'sair':
                break

            resultado = self.analisador.executar(requisito)  # Método que lida com o feedback
            print(f"Resultado: {resultado}")
