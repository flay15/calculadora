class Suma:
    def calcular(self, num1, num2):
        return num1 + num2

class Resta:
    def calcular(self, num1, num2):
        return num1 - num2

class Multiplicacion:
    def calcular(self, num1, num2):
        return num1 * num2

class Division:
    def calcular(self, num1, num2):
        if num2 == 0:
            return "Error: División por cero"
        return num1 / num2

class CalculadoraControlador:
    def __init__(self):
        self.suma = Suma()
        self.resta = Resta()
        self.multiplicacion = Multiplicacion()
        self.division = Division()

    def iniciar_calculadora(self):
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        operacion = input("Seleccione una operación (suma, resta, multiplicacion, division): ").strip().lower()
        
        if operacion == "suma":
            resultado = self.suma.calcular(num1, num2)
        elif operacion == "resta":
            resultado = self.resta.calcular(num1, num2)
        elif operacion == "multiplicacion":
            resultado = self.multiplicacion.calcular(num1, num2)
        elif operacion == "division":
            resultado = self.division.calcular(num1, num2)
        else:
            print("Operación no válida.")
            return

        print(f"El resultado de la {operacion} es: {resultado}")

if __name__ == "__main__":
    calculadora = CalculadoraControlador()
    calculadora.iniciar_calculadora()
