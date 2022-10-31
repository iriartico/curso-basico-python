def ciclo_while(limite):
  contador = 1
  while 2**contador <= limite:
    print('Valor: ' + str(2**contador))
    contador += 1

def tabla(numero):
    print('Esta es la tabla del ' + str(numero))
    for i in range(1,11):
        print(i*numero)

def run():
  LIMITE = 1025
  # ciclo_while(LIMITE)
 

if __name__ == '__main__':
  # run()
  tabla(5)
  