senha = 123456
tentativas = 3
for tentativas in range(3):
    nome = input("digite seu nome: ")
    ds = int(input("digite a senha: "))
    if ds == senha:
        print("Olá seja bem vindo luis")
        exit()
    else:
        trs = tentativas  - (tentativas+1)
        if trs > 0:
            print("você ainda tem {trs} chances")
        else:
            print("Conta bloqueada.")