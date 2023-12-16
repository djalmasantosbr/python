import os

os.getcwd()

os.path.join(os.getcwd(), 'pasta')

os.getcwd() + '\\pasta'

# Retorna a última pasta do caminho
os.path.basename(os.getcwd())

# Através do .split eu digo onde será a quebra e digo a posição que quero entre colchetes
os.getcwd().split('\\')[-1]

# quebrando em forma de tupla usandoos.getcwd
os.path.split(os.getcwd())

# quebrando em forma de tupla usandoos.getcwd e acessando os elementos dela pelo []
os.path.split(os.getcwd())[0]
os.path.split(os.getcwd())[1]

# vai retornar o caminho antes da pasta
os.path.dirname(os.getcwd())


curr_dir = os.getcwd()
lt = os.path.getatime(curr_dir)

from datetime import datetime
datetime.utcfromtimestamp(lt)

os.path.isfile(curr_dir)
os.path.isdir(curr_dir)