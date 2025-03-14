import os

def validate_url(url):
    if not url:
        raise ValueError("Por favor, insira a URL do vídeo!")

def validate_directory(directory):
    if not directory:
        raise ValueError("Por favor, selecione o diretório de destino!")
    if not os.path.exists(directory):
        raise ValueError("O diretório especificado não existe!")
