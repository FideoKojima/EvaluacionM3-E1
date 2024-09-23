# Ejercicio 1
def ejercicio1():
    numeros = []
    while True:
        numero = int(input("Ingresa un número (0 para finalizar): "))
        if numero == 0:
            break
        if len(numeros) < 20:
            numeros.append(numero)
    numeros.sort(reverse=True)
    print("Números ordenados de mayor a menor:", numeros)

# Ejercicio 2
def ejercicio2():
    palabras = set()
    while True:
        palabra = input("Ingresa una palabra (*** para finalizar): ")
        if palabra == "***":
            break
        palabras.add(palabra)
    print("Palabras ingresadas únicas:", palabras)

# Ejercicio 3 - Scrabble
def ejercicio3():
    valores = {
        1: "AEILNORSTU",
        2: "DG",
        3: "BCMP",
        4: "FHVWY",
        5: "K",
        8: "JX",
        10: "QZ"
    }
    
    palabra = input("Ingresa una palabra para obtener su puntaje en Scrabble: ").upper()
    puntaje = 0
    for letra in palabra:
        for key, letras in valores.items():
            if letra in letras:
                puntaje += key
                break
    print(f"El puntaje de la palabra {palabra} es: {puntaje}")

# Ejercicio 4 - Anagramas
def ejercicio4():
    palabra1 = input("Ingresa la primera palabra: ").lower()
    palabra2 = input("Ingresa la segunda palabra: ").lower()
    
    if sorted(palabra1) == sorted(palabra2):
        print("Las palabras son anagramas.")
    else:
        print("Las palabras no son anagramas.")

# Ejercicio 5 - Suma de números
def ejercicio5():
    suma = 0
    while True:
        entrada = input("Ingresa un número (o presiona Enter para finalizar): ")
        if entrada == "":
            break
        try:
            numero = int(entrada)
            suma += numero
        except ValueError:
            print("Error: Ingresa solo números.")
    print(f"La suma total es: {suma}")

# Ejecución de todos los ejercicios
def main():
    ejercicio1()
    ejercicio2()
    ejercicio3()
    ejercicio4()
    ejercicio5()
    print("Programa finalizado.")

if __name__ == "__main__":
    main()
