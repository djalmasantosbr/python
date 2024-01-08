from pathlib import Path 

# Criar caminhos com python


'''
caminho = Path('C:\\Users\\djalm\\OneDrive\\Documentos\\python\\primeria_pasta\\segunda_pasta')

for nome in ['arquivo1.txt', 'arquivo2.txt', 'arquivo3.txt']:
    caminho_arquivo = caminho / nome
    print(caminho_arquivo)
'''
print(Path.home() / 'Documents' / 'assim por diante')