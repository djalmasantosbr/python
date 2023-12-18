# programa para organizar arquivos em pastas

import os


# Criando uma lista com os arquivos da pasta:
arquivo =[]
arquivo = os.listdir()

# Criando um lista com as extenções dos arquivos da pasta:
ext = []
for valor in arquivo:
    ext.append(valor[-3:])

# Limpando extenções repetidas convertendo a lista em um conjunto
a_ext = set(ext)

# Convertendo novamente em lista novamente sem as extenções repetidas
b_ext = []
for valor in a_ext:
    b_ext.append(valor)

# Mostrando os arquivos que pertence a extensão:





