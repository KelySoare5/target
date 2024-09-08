import random

# 1 Questão

def geraFibonacci(max_num):

    fib = [0, 1]
    while True:
        proximo = fib[-1] + fib[-2]

        if proximo > max_num:
            break
        else:
            fib.append(proximo)
    return fib

def perteceFibonacci(numero):

    if numero < 0:
        return "Numeros negativos não pertence a sequência"
    else:
        fibonacciSequencia = geraFibonacci(numero)
    
    if numero in fibonacciSequencia:
        return f"O numero {numero} pertence á sequência"
    else:
        return f"O numero {numero} não pertence á sequência"
    
numeroInformado = random.randint(0, 100)
print(perteceFibonacci(numeroInformado))

