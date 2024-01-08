from pathlib import Path
import os

# Listando arquivos de uma pasta

# print(os.listdir(Path.home()))
#print (os.listdir(Path.cwd()))

#print(list(Path.cwd().glob('*'))) # Esse cria um gerador e para mostrar o caminho a gente precisa usar o list

# Listando arquivos de uma determinada extensão
#print(list(Path.cwd().glob('*.py'))) # Mostra os arquivos com extensão .py

# Listando tudo dentro de uma pasta
#print(list(Path.cwd().glob('**/*')))


# Validando caminhos
#nao_existe = Path.home() / 'nao_existe'
#print(nao_existe.exists())
#print(Path.home().exists())


# Verificando se é arquivo ou pasta
print(Path(__file__))
print(Path(__file__).is_file())

print(Path(__file__).parent)
print(Path(__file__).parent.is_file())

print(Path(__file__).parent)
print(Path(__file__).parent.is_dir())

print(Path(__file__))
print(Path(__file__).is_dir())