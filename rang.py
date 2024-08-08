a = int(input("seu primeiro numero inteiro: "))
b = int(input("seu segundo numero inteiro: "))
soma = 0

if(a < b):
    for termo in range(a,b):
        soma += termo
    print(soma)
else:
    print("Error, tente novamente.")