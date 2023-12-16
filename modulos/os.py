import os

# mostra o caminho onde o arquivo foi criado
os.getcwd()

# mostra todos os aquivos e pastas que esta no diretório
os.listdir()

os.listdir('c:\\Users\\djalm\\OneDrive\\Documentos')

os.listdir('\\Users\\djalm\\OneDrive\\Documentos')

#os.chdir() - para mudar de pasta ou diretório
actual_dir = os.getcwd()
os.chdir('c:\\Users\\djalm\\OneDrive\\Documentos')
print(os.getcwd())
os.chdir(actual_dir)
print(os.getcwd())

# Cria pasta no diretório
os.mkdir('Pasta3')

# Renomeia arquivos ou pastas
os.rename('teste.txt', 'teste2.txt')
os.rename('Pasta3', 'Pasta4')
os.rename('Pasta2','Pasta4/Pasta2')
os.rename('Pasta4/Pasta2', 'Pasta2')

# Remover arquivos
os.remove('teste.csv')

#Remover pastas
os.rmdir('Pasta4')

# Para usar comando que ainda não foram implementados na biblioteca

cmd = 'date'
os.system(cmd)



