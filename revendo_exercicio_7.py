from pathlib  import Path

# Desenvolva um script para encontrar um aquivo dentro da pasta home do usuário

caminho = Path.home()

# usando .name para encontrar arquivo com extensão
for arquivo in caminho.glob('**/*'):
    if arquivo.is_file():
        if arquivo.name == '3_construindo_caminhos.py':
            print(arquivo)
            
# usando .stem para encontrar arquivo sem extensão
for arquivo in caminho.glob('**/*'):
    if arquivo.is_file():
        if arquivo.stem == '3_construindo_caminhos.py':
            print(arquivo)

# Função para encontrar arquivo

def encontra_arquivo(caminho, nome_do_arquivo):
    for arquivo in caminho.glob('**/*'):
        if arquivo.is_file():
            if arquivo.stem == nome_do_arquivo:
                print(arquivo)

encontra_arquivo(Path.cwd(), 'arquivo1')