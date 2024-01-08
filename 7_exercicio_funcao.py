from pathlib import Path

# Desenvolva uma função para encontrar um arquivo dentro da pasta home do usuário

def encontra_arquivo(caminho, nome_do_arquivo):
    for arquivo in caminho.glob('**/*'):
        if arquivo.is_file():
            if arquivo.stem == nome_do_arquivo:
                print(arquivo)
    

encontra_arquivo(Path.home(),'ressonancia_lombar.pdf')