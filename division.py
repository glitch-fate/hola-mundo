try:
    num1 = float(input("Introduce el numerador: "))
    num2 = float(input("Introduce el denominador: "))
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")      
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError:
    print("Error: Entrada no válida. Por favor, introduce números válidos.")