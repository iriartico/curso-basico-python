def es_primo(num):
    contador = 0
    for i in range(1, num+1):
        if num % i == 0 and num != 1:
            contador += 1
    return contador


def run():
    numero = int(input('Ingresa un numero: '))
    if es_primo(numero) == 2:
        print('Es un numero primo')
    else:
        print('No es un numero primo')


if __name__ == '__main__':
    run()

