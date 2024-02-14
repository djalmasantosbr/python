from pathlib import Path
import os
# Aula 5 - Lendo e escrevendo arquivos

# Retornando caminho absoluto
print(Path.cwd())

# Esse caminho é absoluto

print(Path.cwd().is_absolute())

# Retornando camino da primeira pasta
print(Path('primeira_pasta'))

# Esse caminho é absoluto
print(Path('primeira_pasta').is_absolute())

# Transformando o caminho em absoluto

print(Path.cwd() / 'primeira_pasta') # Primeiro exemplo
print((Path.cwd() / 'primeira_pasta').exists()) # para saber se a pasta existe

os.chdir(Path.home()) # Trocando de pasta
print(Path.cwd() / 'primeira_pasta') # Primeiro exemplo
print((Path.cwd() / 'primeira_pasta').exists()) # para saber se a pasta existe

# Garantindo que estamos retornando o caminho para a pasta do script

print(__file__)
print(Path(__file__)) # Busca o caminho absoluto
print(Path(__file__).is_absolute()) # condição que verifica se o caminho é absoluto
print(Path(__file__).parent) # retorna onde a pasta onde o arquivo esta contido
print(Path(__file__).parent / 'primeira_pasta')
print((Path(__file__).parent / 'primeira_pasta').exists())

# trabalhando com partes de caminho

caminho_arquivo = Path(__file__)

print(caminho_arquivo) # mostra o caminho da pasta atual
print(caminho_arquivo.anchor) # Mostra a pasta raiz
print(caminho_arquivo.parent) # Vai retornando a pasta a cada .parent acrescentado
print(caminho_arquivo.name) # Mostra o nome do arquivo 
print(caminho_arquivo.stem) # A base do nome sem extenção
print(caminho_arquivo.suffix) # mostra a extenção do arquivo
print(caminho_arquivo.drive) # mostra o diretório

# Diferenta entre .parent e .parents

print(caminho_arquivo.parent)
print(caminho_arquivo.parents[0])

print(caminho_arquivo.parent.parent)
print(caminho_arquivo.parents[1])

print(caminho_arquivo.parent.parent.parent)
print(caminho_arquivo.parents[2])

# Aula 6 - Lendo e escrevendo arquivos

# Listando arquivo de uma pasta

print(os.listdir(Path.cwd())) # Lista os arquivos no diretório

print(Path.cwd().glob('*')) # Lista todos os caminhos absolutos em forma de generator

print(list(Path.cwd().glob('*'))) # Usando o comando list para mostrar todos os caminhos absolutos

# Listando arquivos de uma determinada extensão

print(list(Path.cwd().glob('*.py')))

# Listar tudo dentro de uma pasta

print(list(Path.cwd().glob('**/*'))) # mostra todos os arquvos em pastas e subpastas

# Validando caminhos

print(Path.home().exists()) # verifica se o caminho existe

nao_existe = Path.home() / 'nao_existe'
print(nao_existe.exists())

# Verificando se é arquivo ou pasta

print(Path(__file__))
print(Path(__file__).is_file()) # o comando .is_file esta perguntando se é um arquivo



