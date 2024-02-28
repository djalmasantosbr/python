from pathlib import Path
import shutil

# Criando pastas
pasta_atual = Path(__file__).parent
caminho_pasta_destino = pasta_atual / 'destino4'


caminho_pasta_destino.mkdir(exist_ok=True) # criando a pasta e uma condição exist_ok=True para verificar se a pasta já existe

# Criando pasta com todos as pastas anteriores necessárias
pasta_atual = Path(__file__).parent
caminho_pasta_destino = pasta_atual / 'destino5' / 'destino51'

caminho_pasta_destino.mkdir(parents=True) # cria pasta com subpastas com a condição parents=True

# Copiando pastas
pasta_atual = Path(__file__).parent
shutil.copytree(pasta_atual / 'destino5', pasta_atual / 'destino1' / 'destino5')

# Deletando pastas vazias
pasta_atual = Path(__file__).parent
pasta_remover = pasta_atual / 'destino5' / 'destino51'
pasta_remover.rmdir() # Deleta pastas vazias

# Deletando pastas com conteúdo
pasta_atual = Path(__file__).parent
pasta_remover = pasta_atual / 'destino1' 
shutil.rmtree(pasta_remover)


# Compactando arquivos
pasta_atual = Path(__file__).parent
pasta_a_ser_compactada = pasta_atual
nome_arquivo = pasta_atual / 'compactado'

shutil.make_archive(nome_arquivo, 'zip',pasta_a_ser_compactada)

# Descompactando arquivos
pasta_atual = Path(__file__).parent
nome_arquivo = pasta_atual / 'compactado.zip'
pasta_descompactada = pasta_atual / 'descompactada'

shutil.unpack_archive(nome_arquivo,pasta_descompactada, 'zip')
