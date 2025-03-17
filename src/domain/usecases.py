#lógica central do sistema para a nálise de pontos de função
#faz a integração da memória, da base de conhecimento e da integração com o GPT
#principal logal onde ocorre o ciclo do ReAct

#duas alterações: 1- melhora na equivalência semântica 2 - quando o usuário sugerir um ponto de função diferente, o sistema deve validar se a sugestão é válida com o modelo
from src.infra.openai_api import GPTAnalyzer

class AnalisarPontoFuncao:
    def __init__(self, knowledge_base, memory):
        self.knowledge_base = knowledge_base
        self.memory = memory
        self.analyzer = GPTAnalyzer()

    def executar(self, requisito):
        # Verifica se o requisito já foi analisado (considerando equivalência semântica)
        requisito_equivalente = self.verificar_equivalencia(requisito)
        if requisito_equivalente:
            resultado_armazenado = self.memory.retrieve(requisito_equivalente)
            return (
    "\n------------------------------------------------------------------------------------"
    "\nResultado encontrado na memória para um requisito equivalente na contagem de pontos de Função. Segue resultado da análise:"
    "\n--------------------------------------------------------------------------------------"
        f"\n{resultado_armazenado}" )

        # Se não tiver um resultado armazenado, faz a análise
        pontos_funcao = self.analisar_requisito(requisito)

        # Armazena o resultado para futuras referências
        self.memory.store(requisito, pontos_funcao)

        while True:
            # Solicita feedback do usuário
            feedback = input(f"{pontos_funcao} A estimativa de pontos de Função está correta? (sim/não): ")
            
            if feedback.lower() == "sim":
                self.memory.store(requisito, pontos_funcao)  # Armazena o requisito confirmado
                return f"Estimativa confirmada e armazenada."
            
            elif feedback.lower() == "não":
                pontos_corrigidos = int(input("Por favor, insira o valor correto dos Pontos de Função: "))
                
                # Solicita uma nova análise ao modelo com o valor corrigido
                pontos_funcao_revisado = self.reanalisar_requisito(requisito, pontos_corrigidos)
                self.memory.store(requisito, pontos_funcao_revisado)  # Armazena a versão revisada
                return f"Resultado revisado: {pontos_funcao_revisado} Pontos de Função."
            
            else:
                print("Resposta inválida. Digite 'sim' ou 'não'.")

    def analisar_requisito(self, requisito):
        # Usa a API da OpenAI para analisar o requisito com base nas regras
        return self.analyzer.analisar(requisito, self.knowledge_base.get_regras())

    def reanalisar_requisito(self, requisito, pontos_corrigidos):
        # Usa a API da OpenAI para refazer a análise considerando o novo valor
        novo_prompt = f"""
        O usuário corrigiu a estimativa para {pontos_corrigidos} Pontos de Função.
        Refaça a contagem de Pontos de Função para o seguinte requisito:
        "{requisito}"
        e explique sua análise com base nas regras.
        """
        return self.analyzer.analisar(novo_prompt, self.knowledge_base.get_regras())
    
    def verificar_equivalencia(self, novo_requisito):
        """ Verifica se um novo requisito é semanticamente equivalente a algum já armazenado. """
        for requisito_armazenado in self.memory.past_requisicoes.keys():
            prompt_equivalencia = f"""
            Considere os seguintes requisitos:

            Requisito armazenado: "{requisito_armazenado}"
            Novo requisito: "{novo_requisito}"

            Eles representam a mesma funcionalidade e possuem equivalência semântica no contexto de análise de pontos de função?
            Retorne apenas 'sim ou 'não'.
            """
            resposta = self.analyzer.analisar(prompt_equivalencia, [])
            
            if "sim" in resposta.lower():
                return requisito_armazenado
            
        return None  # Retorno caso não haja equivalência



'''
    def verificar_equivalencia(self, novo_requisito):
        """ Verifica se um novo requisito é semanticamente equivalente a algum já armazenado. """
        for requisito_armazenado in self.memory.past_requisicoes.keys():
            prompt_equivalencia = f"""
            Considere os seguintes requisitos:
            
            Requisito armazenado: "{requisito_armazenado}"
            Novo requisito: "{novo_requisito}"

            Eles representam a mesma funcionalidade e possuem equivalência semântica no contexto de análise de pontos de função?
            Responda com 'sim' ou 'não'.
            """
            resposta = self.analyzer.analisar(prompt_equivalencia, [])
            if "sim" in resposta.lower():
                return requisito_armazenado  # Retorna o requisito equivalente

        return None  # Caso não encontre equivalência



class AnalisarPontoFuncao:
    def __init__(self, knowledge_base, memory):
        self.knowledge_base = knowledge_base
        self.memory = memory
        self.analyzer = GPTAnalyzer()

    def executar(self, requisito):
        # Tenta recuperar um resultado anterior da memória
        resultado_armazenado = self.memory.retrieve(requisito)
        if resultado_armazenado:
            return f"Resultado encontrado na memória: {resultado_armazenado} Pontos de Função."

        # Se não tiver um resultado armazenado, faz a análise
        pontos_funcao = self.analisar_requisito(requisito)

        # Armazena o resultado para futuras referências
        self.memory.store(requisito, pontos_funcao)

        # Solicita feedback do usuário
        feedback = input(f"A estimativa de {pontos_funcao} Pontos de Função está correta? (sim/não): ")
        if feedback.lower() == "não":
            pontos_corrigidos = int(input("Por favor, insira o valor correto dos Pontos de Função: "))
            self.memory.store(requisito, pontos_corrigidos)
            return f"Resultado corrigido: {pontos_corrigidos} Pontos de Função."

        return f"Estimativa de Pontos de Função: {pontos_funcao}"
    def analisar_requisito(self, requisito):
        # Usa a API da OpenAI para analisar o requisito com base nas regras
        return self.analyzer.analisar(requisito, self.knowledge_base.get_regras())
'''