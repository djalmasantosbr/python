from pathlib import Path

# Desenvolva um script para encntrar um arquivo dentro da pasta home do usuário

digite_arquivo = input("Digite o nome do arquivo com sua extensão:\n")
caminho = Path.home()

for arquivo in caminho.glob('**/*'):
    if arquivo.is_file():
        if arquivo.name == digite_arquivo: # . name preciso colocar a extenção .stem não precisa colocar a extensão do arquivo
            print(arquivo)
            
