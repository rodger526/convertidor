
def peso_mexicano():
    print('\n--- Convertir desde Peso Mexicano ---')
    valor = float(input('Ingrese la cantidad en pesos mexicanos: '))
    valor_dolar = round(valor * 0.05415, 2)
    print(f'Dólares: ${valor_dolar}')
    valor_euro = round(valor * 0.04623, 2)
    print(f'Euros: €{valor_euro}')
    valor_peruano = round(valor * 0.18413, 2)
    print(f'Soles peruanos: S/{valor_peruano}')
    valor_argentino = round(valor * 73.45, 2)
    print(f'Pesos argentinos: ${valor_argentino}')

def dolar():
    print('\n--- Convertir desde Dólar ---')
    valor = float(input('Ingrese la cantidad en dólares: '))
    valor_mexico = round(valor * 18.36, 2)
    print(f'Pesos mexicanos: ${valor_mexico}')
    valor_euro = round(valor * 0.8579, 2)
    print(f'Euros: €{valor_euro}')
    valor_peruano = round(valor * 3.5043, 2)
    print(f'Soles peruanos: S/{valor_peruano}')
    valor_argentino = round(valor * 1348.604, 2)
    print(f'Pesos argentinos: ${valor_argentino}')

def peso_argentino():
    print('\n--- Convertir desde Peso Argentino ---')
    valor = float(input('Ingrese la cantidad en pesos argentinos: '))
    valor_dolar = round(valor * 0.00074, 2)
    print(f'Dólares: ${valor_dolar}')
    valor_euro = round(valor * 0.00063, 2)
    print(f'Euros: €{valor_euro}')
    valor_mexico = round(valor * 0.01362, 2)
    print(f'Pesos mexicanos: ${valor_mexico}')
    valor_peruano = round(valor * 0.0026, 2)
    print(f'Soles peruanos: S/{valor_peruano}')

def sol_peruano():
    print('\n--- Convertir desde Sol Peruano ---')
    valor = float(input('Ingrese la cantidad en soles peruanos: '))
    valor_dolar = round(valor * 0.2854, 2)
    print(f'Dólares: ${valor_dolar}')
    valor_euro = round(valor * 0.2448, 2)
    print(f'Euros: €{valor_euro}')
    valor_mexico = round(valor * 5.24, 2)
    print(f'Pesos mexicanos: ${valor_mexico}')
    valor_argentino = round(valor * 384.85, 2)
    print(f'Pesos argentinos: ${valor_argentino}')

def euro():
    print('\n--- Convertir desde Euro ---')
    valor = float(input('Ingrese la cantidad en euros: '))
    valor_dolar = round(valor * 1.1656, 2)
    print(f'Dólares: ${valor_dolar}')
    valor_mexico = round(valor * 21.40, 2)
    print(f'Pesos mexicanos: ${valor_mexico}')
    valor_peruano = round(valor * 4.085, 2)
    print(f'Soles peruanos: S/{valor_peruano}')
    valor_argentino = round(valor * 1572.15, 2)
    print(f'Pesos argentinos: ${valor_argentino}')


while True:

    print('============convertidor=============')
    print('elija una  para darle el valor en diferentes')
    print('convertidor de monedas \n1.peso mexicano\n2.dolar\n3.peso argentino\n4.sol peruano\n5.euro')
    opcion=input('ingrese que tipo de valor va a ingresar: ')
    if opcion=='1':
        peso_mexicano()
    elif opcion=='2':
        dolar()
    elif opcion=='3':
        peso_argentino()
    elif opcion=='4':
        sol_peruano()
    elif opcion=='5':
        euro()
    elif opcion=='6':
        print('hasta luego')
        break
    else:
        print(f'opcion invalida, {opcion} es un valor que no existe')
        print('\nPresione enter para continuar')