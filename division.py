def division(a, b):
    if b == 0:
        print("No se puede dividir entre cero")
        return 0
    resultado = a / b
    print("El resultado de {} / {} es {}".format(a, b, resultado))
    return resultado