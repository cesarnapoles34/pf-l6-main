
def trivia_fetch(num):
    if num % 2 == 0:
        texto = f"{num} es un número par."
    else:
        texto = f"{num} es un número impar."
 
    trivia = {
        "number": num,
        "text": texto
    }
 
    return trivia
 
 
def main():
    while True:
        entrada = input("Ingresa un número (o escribe 'salir' para terminar): ")
 
        if entrada.lower() == "salir":
            print("¡Hasta luego!")
            break
 
        numero = int(entrada)
        trivia = trivia_fetch(numero)
        print(trivia)
 
 
if __name__ == "__main__":
    main()

 