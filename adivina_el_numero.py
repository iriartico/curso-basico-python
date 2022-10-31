import random


def run():
    aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Ingrese un numero del 1 al 100: '))
    while numero_elegido != aleatorio:
        if numero_elegido < aleatorio:
            print('Elige un numero mas grande')
        else:
            print('Elige un numero mas pequeno')
        numero_elegido = int(input('Elige otro numero: '))
    print('Ganaste')


if __name__ == '__main__':
    run()
