
def sumar(num1 ,num2):
    return num1 + num2

def restar(num1 ,num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    try:
        a = num1 / num2
    except ZeroDivisionError:
        return "La division entre cero no es valida"
