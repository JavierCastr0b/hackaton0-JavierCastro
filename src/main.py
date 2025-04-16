def calculate(expression: str) -> float:
    if "+" in expression:
        a, b = map(float, expression.split("+"))
        return a + b
    raise NotImplementedError("Operación no soportada")

def main():
    print("Calculadora - Escribe una operación (ej. 2 + 2). Presiona 'c' para borrar.")
    while True:
        entrada = input(">> ")
        if entrada.strip().lower() == "c":
            print("Entrada borrada.")
            continue
        try:
            resultado = calculate(entrada)
            print("Resultado:", resultado)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
