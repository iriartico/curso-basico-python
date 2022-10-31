def conversor(tipo_moneda, valor_dolar):
  quatitie = input("Cuantos " + tipo_moneda + " tienes?: ")
  quatitie = float(quatitie)
  dolares = quatitie/valor_dolar
  dolares = round(dolares, 2)
  dolares = str(dolares)
  print("Tienes actualmente: " + dolares + " $")


# Menu de inicio
menu = """
Bienvenido al conversor de monedas

1 - Bolivianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elija una opcion: """

opcion = int(input(menu))

if opcion == 1:
  conversor("bolivianos", 6.96)
elif opcion ==2:
  conversor("pesos argentinos", 150.04)
elif opcion == 3:
  conversor("pesos mexicanos", 20.04)
else:
  print("Por favor, ingrese una opcion valida")