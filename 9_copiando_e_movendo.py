from pathlib import Path
import shutil
import os

# Copiando arquivo com copyfile
pasta_atual = Path(__file__).parent # Garante que esta na pasta atual
caminho_arquivo = pasta_atual / 'texto.txt' # arquivo ser copiado
caminho_arquivo_destino = pasta_atual / 'destino1' / 'texto.txt' # copiando o arquivo para o destino

shutil.copyfile(caminho_arquivo, caminho_arquivo_destino) # Comando para copiar arquivo

# copiando arquivo com copy - copia sem os metadados e sem permissões
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino2'

shutil.copy(caminho_arquivo, caminho_pasta_destino)

# Copiando arquivo com copy2 - copia com todas as informações e metadados
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino3'

shutil.copy2(caminho_arquivo, caminho_pasta_destino)

# Movendo arquivos
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino1'

shutil.move(caminho_arquivo, caminho_pasta_destino) # comando para mover arquivo

# Outro exemplo de movendo arquivos
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino2' / 'texto.txt'

shutil.move(caminho_arquivo, caminho_pasta_destino)

# Deletando arquivos
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino3' / 'texto.txt'

shutil.copyfile(caminho_arquivo, caminho_pasta_destino)

if caminho_arquivo.exists():
    os.remove(caminho_arquivo) # deleta o arquivo 