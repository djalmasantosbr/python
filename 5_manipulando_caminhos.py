from pathlib import Path
import os
'''
# Retornando caminho do diretório de trabalho atual
print(Path.cwd())

# Esse caminho é absoluto
print(Path.cwd().is_absolute())

# Retornando caminho da primeira pasta
print(Path('primeira_pasta'))

# Esse caminho é absoluto
print(Path('primeira_pasta').is_absolute())
'''

# Transformando o caminho em absoluto "Não é acoselhado usar esse caminho porque dar erro"
"""
print(Path.cwd() / 'primeira_pasta')
print((Path.cwd() / 'primeira_pasta').exists())

os.chdir(Path.home())
print(Path.cwd() / 'primeira_pasta')
print((Path.cwd() / 'primeira_pasta').exists())
"""

# Garantindo que estamos retornando o caminho a pasta script
'''
print(__file__)
print(Path(__file__))
print(Path(__file__).is_absolute())
print(Path(__file__).parent)

# Criando pasta
print(Path(__file__).parent / 'primeira_pasta')
print((Path(__file__).parent / 'primeira_pasta').exists())
'''

# Trabalhando com partes do caminho
caminho_arquivo = Path(__file__) # caminho do nosso arquivo

print(caminho_arquivo) # Mostra o caminho do arquivo
print(caminho_arquivo.anchor) # Mostra a pasta raiz
print(caminho_arquivo.parent) # Pasta anterior
print(type(caminho_arquivo.parent)) # Mostra o tipo da variável
print(caminho_arquivo.parent.parent)# .parent vai retornando uma pasta anterior
print(caminho_arquivo.name) # Faz o caminho absoluto para aquele arquivo.
print(caminho_arquivo.stem) # Mostra a base do nome
print(caminho_arquivo.suffix) # Mostra o sulfixo ou extenção do arquivo
print(caminho_arquivo.drive) # Mostra o nome do nosso drive . Exemplo "c:"

print(caminho_arquivo.parent)
print(caminho_arquivo.parents[1]) # Retorna para pasta anterior de uma forma mais fácil: 1 volta uma pasta, 2 volta duas pasta e assim por diante.


