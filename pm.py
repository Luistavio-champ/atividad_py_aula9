primeirotermo = int(input("Digite o primeiro termo da PA: "))
quanttermo = int(input("Digite a quantidade de termos da PA: "))
razao = int(input("Digite a razão da PA: "))
s = 0
for y in range(primeirotermo,quanttermo + 1,razao):
    s+=y
print(s)