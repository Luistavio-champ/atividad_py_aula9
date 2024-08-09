medicamentobarato = ""
precobarato = float("inf")
soma = 0


for x in range(5):
    med = input("nome do medicamento: ")
    preco = float(input("preço do medicamento em R$: "))

    if preco < precobarato:
        precobarato = preco
        medicamentobarato = med
    soma += x
media = soma / 5
print(medicamentobarato , precobarato, media)