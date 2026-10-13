def conversor():
    print("--- CONVERSOR DE BASES NUMÉRICAS ---")
    print("1. Decimal a Binario, Octal y Hexadecimal")
    print("2. Binario, Octal o Hexadecimal a Decimal")
    
    opcion = input("Elige una opción (1 o 2): ")
    
    if opcion == "1":
        try:
            decimal = int(input("Introduce el número decimal: "))
            print(f"Binario: {bin(decimal)[2:]}")
            print(f"Octal: {oct(decimal)[2:]}")
            print(f"Hexadecimal: {hex(decimal)[2:].upper()}")
        except ValueError:
            print("Error: Por favor, introduce un número entero válido.")
            
    elif opcion == "2":
        print("¿De qué base vienes?")
        print("a) Binario\nb) Octal\nc) Hexadecimal")
        sub_op = input("Elige (a/b/c): ").lower()
        
        numero_str = input("Introduce el número a convertir: ")
        
        bases = {'a': 2, 'b': 8, 'c': 16}
        if sub_op in bases:
            try:
                decimal = int(numero_str, bases[sub_op])
                print(f"Resultado en Decimal: {decimal}")
            except ValueError:
                print("Error: El número no corresponde a la base numérica seleccionada.")
        else:
            print("Opción de base inválida.")
    else:
        print("Opción principal no válida.")

if __name__ == "__main__":
    conversor()