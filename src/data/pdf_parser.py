import PyPDF2
#PyPDF2 faz a leitura do arquivo e converte seu conteudo em texto
#o texto extraído é usado como base de regras do sistema
class PDFParser:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_text(self):
        with open(self.pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
        return text
