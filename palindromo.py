def palindromo(word):
    word = word.replace(' ', '').lower()
    if word == word[::-1]:
        print('Es palindromo')
    else:
        print('No es palindromo')


def run():
    entrada = input('Ingrese una palabra: ')
    palindromo(entrada)

if __name__ == '__main__':
  run()