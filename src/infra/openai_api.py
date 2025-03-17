import os
import openai
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env (se existir)
load_dotenv()

class GPTAnalyzer:
    def __init__(self):
        # Obtém a chave da API da OpenAI da variável de ambiente
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("A chave da API da OpenAI não foi encontrada. Defina OPENAI_API_KEY no .env ou nas variáveis de ambiente.")

        # Configuração do cliente OpenAI
        self.client = openai.OpenAI(api_key=self.api_key)

    def analisar(self, descricao_requisito, regras):
        prompt = f"""
        Regras para contagem de pontos de função:
        {regras}

        Dado o seguinte requisito:
        "{descricao_requisito}"

        Calcule a quantidade estimada de pontos de função e explique sua análise.
        """
        resposta = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return resposta.choices[0].message.content

