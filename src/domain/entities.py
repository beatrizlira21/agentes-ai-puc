#definição das entidades principais do sistema. aqui é estabelecia uma estrutura de dados pra o sistema manipular

class Requisito:
    def __init__(self, id: int, descricao: str):
        self.id = id
        self.descricao = descricao

class AnalisePontoFuncao:
    def __init__(self, requisito: Requisito, pontos_de_funcao: float):
        self.requisito = requisito
        self.pontos_de_funcao = pontos_de_funcao
