from abc import ABC, abstractmethod

class KnowledgeBaseRepository(ABC):
    #interface para acessar as regras de negócio da base de conhecimento
    @abstractmethod
    def get_rules(self) -> list:
        pass

class MemoryRepository(ABC):
    #armazena e recupera as análises anteriores para gerar o contexto
    @abstractmethod
    def save_analysis(self, analise):
        pass

    @abstractmethod
    def get_previous_analysis(self, requisito_id):
        pass
