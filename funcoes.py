def somar(num1, num2):
    resultado = num1 + num2
    return resultado

def subtrair(num1, num2):
    resultado = num1 - num2
    return resultado

def multiplicar(num1, num2):
    resultado = num1 * num2
    return resultado

def dividir(num1, num2):
    if num2 == 0:
        return "Erro"
    resultado = num1 / num2
    return resultado

def porcentagem(num1, num2):
    if num1 == 0:
        return num2/100
    resultado = (num1 / 100) * num2
    return resultado