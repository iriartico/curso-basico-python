def run():
    # Imprimiendo los numeros pares de un rango de numeros
    # for contador in range(1, 51):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # Creando una excepion a un numero
    # for i in range(100):
    #   print(i)
    #   if i == 5:
    #     break

    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)


if __name__ == '__main__':
    run()
