#ReAct foi implementado neste sistema com os ciclos de observação, raciocínio, ação e aprendizado contínuo.
#OBSERVAÇÃO acontece na análise do requisito, verificando se ele ja foi analisado anteriormente, fazendo uma consulta na memória
#RACIOCÍNIO usa o ChatGpt para anlisar os requisitos se baseando nas regras de pontos de função, combinando com o arquivo da base de conhecimento com o prompt
#AÇÃO armazena os resultados para uso futuro, apresenta as estimativas ao usuário e solicita o feedback
#APRENDIZADO CONTINUO incorpora o feedback para correção do que for identificado por ele como incorreto, atualiza a memória e cria um ciclo de melhoria contínua.

from src.interface.cli import CLI

if __name__ == "__main__":
    pdf_path = "guia-ponto-funcao.pdf"  # Caminho do PDF
    cli = CLI(pdf_path)
    cli.iniciar()
