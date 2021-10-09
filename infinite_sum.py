res = 0
print('Escribe un número y "basta" para salir')
while True:
    user = input('Escribe un número aquí: ')
    if user == 'basta':
        break
    try:
        res += float(user)
    except ValueError:
        print('Dato inválido')
        exit()
print(res)


