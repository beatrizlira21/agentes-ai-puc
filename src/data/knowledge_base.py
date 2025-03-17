from .pdf_parser import PDFParser
#from ..domain.repository import KnowledgeBaseRepository
#implementa base de conhecimento a partir da extração do conteúdo do arquivo .pdf
#essa parte do código que representa o "conhecimento do domínio" do paradigma ReAct

class KnowledgeBase:
    def __init__(self, pdf_path="guia-ponto-funcao.pdf"):
        #PDFParser é responsável por extrair o texto do arquivo
        self.regras = PDFParser(pdf_path).extract_text().split("\n")
    
    def get_regras(self):
        return self.regras
