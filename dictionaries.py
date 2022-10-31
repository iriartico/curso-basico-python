def run():
    my_dictionary = {
        'key1': 1,
        'key2': 2,
        'key3': 3,
    }
    # print(my_dictionary)
    # print(my_dictionary['key3'])

    poblacion_paises = {
        'Argentina': 23563,
        'Brasil': 563421,
        'Italia': 2356,
    }
    # print(poblacion_paises['Brasil'])

    # for pais in poblacion_paises.keys():
    #   print(pais)

    # for pais in poblacion_paises.values():
    #   print(pais)

    for pais, poblacion in poblacion_paises.items():
        print('- ' + pais + ' tiene una poblacion de ' +
              str(poblacion) + ' habitantes')


if __name__ == '__main__':
    run()
