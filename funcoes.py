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
        return "Não é possível dividir por 0"
    resultado = num1 / num2
    return resultado

def porcentagem(num1, num2):
    resultado = (num1 / 100) * num2
    return resultado