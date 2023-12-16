import os

escolha = {
    "0": "Mostrar portifólio",
    "1": "Alugar um carro",
    "2": "Devolver um carro",
}

modelo = {
    
    "Chevrolet Traker ": 120,
    "Chevrolet Onix": 90,
    "Chevrolet Spin": 150,
    "Hyundai HB20": 85,
    "Hyundai Tucson": 120,
    "Fiat Uno": 60,
    "Fiat Mobi": 70,
    "Fiat Pulse": 130,
}

alugado = {}

while  True:
    os.system("cls")  
    print("==============================")
    print("Bem vindo à locadora de carros")
    print("==============================")
    print("")
    print("O que deseja fazer?")
    print("")

    i = 0
    for op, escolha1 in escolha.items():
        print(i, ":", escolha1)
        i += 1
    op = int(input())
    
    # Mostra os modelos disponíveis
    if op == 0:
        os.system("cls")
        y = 0
        print("[PORTIFOLIO] - Conheça nossos modelos disponíveis:")
        print("")
        for veiculo, valor in modelo.items():
            print("[",y,"] - ", veiculo,"- R$", valor," / dia." )
            y += 1
    # Escolhe o modelo e quantos dias escolhidos, mostra os dias alugados e o valor a pagar, Adiciona o modelo no dicionário alugado e exclui do dicionário modelo.
    elif op == 1:
        os.system("cls")
        y = 0
        print("[ ALUGAR ] - Dê uma olhada em nosso Portifólio:")
        print("")
        for veiculo, valor in modelo.items():
            print("[",y,"] - ", veiculo,"- R$", valor," / dia." )
            y += 1
        print("")
        print("Digite o código do modelo que deseja alugar:")
        print("")
        y = int(input())
        print("")
        print("Por quantos dias deseja alugar:")
        dia = int(input())
        t = list(modelo.items())[y]
        os.system("cls")
        print("[ALUGANDO]")
        print("Modelo escolhido: {} por {} dia(s).".format(t[0], dia))  
        print("O aluguel totalizaria R$ {}. Deseja alugar: 0 - SIM | 1 - NÃO?".format(t[1] * dia))
        alog = int(input())
        if alog == 0:          
            alugado[t[0]]=t[1]
            modelo.pop(t[0])  
            os.system("cls")
            print("Alugado com sucesso...")
        else:
            os.system("cls")
    # Lista os modelos alugados e pede para escolher o carro que será devolvido, exclui o modelo do dicionário alugado e adiciona no dicionário modelo.
    elif op == 2:
        if alugado == {}:
            os.system("cls")
            print("[ ALUGAR ] - Não ha modelo alugado no momento...")        
        else:   
            os.system("cls")
            y = 0
            print("")
            for veiculo, valor in alugado.items():
                print("[",y,"] - ", veiculo,"- R$", valor," / dia." )
                y += 1
            print("")
            print("[DEVOLUÇÃO] - Digite o código do modelo a ser devolvido:")
            dev = int(input())
            d = list(alugado.items())[dev]
            modelo[d[0]]=d[1]
            alugado.pop(d[0])
            os.system("cls")
            print("Modelo {} devolvido com sucesso...".format(d[0]))
    print("")
    print("Continuar no sistema? 0 - SIM | 1 - NÃO")  
    cont = int(input()) 
    if cont == 1:
        os.system("cls")
        break 
    else:
        os.system("cls")


    