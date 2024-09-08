# 5 Questão

def inverter_string(s):

    lista = list(s)
    inicio = 0
    fim = len(lista) - 1
    
    while inicio < fim:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
        inicio += 1
        fim -= 1
    
    return ''.join(lista)

entrada = input("Digite a string que deseja inverter: ")

resultado = inverter_string(entrada)
print("String invertida:", resultado)
