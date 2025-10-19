# Diccionario de tasas de cambio
tasas = {
    "MXN": {"USD": 0.05415, "EUR": 0.04623, "PEN": 0.18413, "ARS": 73.45},
    "USD": {"MXN": 18.36, "EUR": 0.8579, "PEN": 3.5043, "ARS": 1348.604},
    "ARS": {"USD": 0.00074, "EUR": 0.00063, "MXN": 0.01362, "PEN": 0.0026},
    "PEN": {"USD": 0.2854, "EUR": 0.2448, "MXN": 5.24, "ARS": 384.85},
    "EUR": {"USD": 1.1656, "MXN": 21.40, "PEN": 4.085, "ARS": 1572.15}
}

# Diccionario de fórmulas de conversión de temperatura
def to_celsius(valor, escala):
    if escala == "C": return valor
    elif escala == "F": return (valor - 32) * 5/9
    elif escala == "K": return valor - 273.15
    elif escala == "R": return (valor - 491.67) * 5/9
    elif escala == "Re": return valor * 5/4
    elif escala == "De": return 100 - (valor * 2/3)
    elif escala == "N": return valor * 100/33
    elif escala == "Ro": return (valor - 7.5) * 40/21

def from_celsius(valor, escala):
    if escala == "C": return valor
    elif escala == "F": return (valor * 9/5) + 32
    elif escala == "K": return valor + 273.15
    elif escala == "R": return (valor + 273.15) * 9/5
    elif escala == "Re": return valor * 4/5
    elif escala == "De": return (100 - valor) * 3/2
    elif escala == "N": return valor * 33/100
    elif escala == "Ro": return (valor * 21/40) + 7.5

def convertir_temperatura():
    print("\n========== CONVERTIDOR DE TEMPERATURA ==========")
    print("Escalas disponibles:")
    print("C - Celsius | F - Fahrenheit | K - Kelvin | R - Rankine")
    print("Re - Réaumur | De - Delisle | N - Newton | Ro - Rømer")

    origen = input("\nIngrese la escala base: ").strip()
    destino = input("Ingrese la escala destino: ").strip()

    try:
        valor = float(input(f"Ingrese el valor en {origen}: "))
    except ValueError:
        print("⚠️ Error: Debe ingresar un número válido.")
        return

    try:
        celsius = to_celsius(valor, origen)
        convertido = round(from_celsius(celsius, destino), 2)
        print(f"\n{valor} {origen} equivalen a {convertido} {destino}\n")
    except Exception:
        print("⚠️ Escala no válida. Verifique su ingreso.")


# Función general de conversión de moneda
def convertir_moneda(moneda_base):
    print(f'\n--- Convertir desde {moneda_base} ---')
    
    try:
        valor = float(input(f'Ingrese la cantidad en {moneda_base}: '))
    except ValueError:
        print("⚠️ Error: Debe ingresar un número válido.")
        return

    for destino, tasa in tasas[moneda_base].items():
        convertido = round(valor * tasa, 2)
        print(f'{destino}: {convertido}')

# MENÚ PRINCIPAL
while True:
    print('\n================= CONVERTIDOR =================')
    print('1. Convertidor de Monedas')
    print('2. Convertidor de Temperaturas')
    print('3. Salir')

    opcion = input('\nSeleccione una opción: ')

    if opcion == '1':
        print('\n--- MONEDAS DISPONIBLES ---')
        print('1. Peso Mexicano (MXN)')
        print('2. Dólar (USD)')
        print('3. Peso Argentino (ARS)')
        print('4. Sol Peruano (PEN)')
        print('5. Euro (EUR)')
        print('6. Volver')
        sub = input('\nSeleccione una opción: ')

        if sub == '1': convertir_moneda("MXN")
        elif sub == '2': convertir_moneda("USD")
        elif sub == '3': convertir_moneda("ARS")
        elif sub == '4': convertir_moneda("PEN")
        elif sub == '5': convertir_moneda("EUR")
        elif sub == '6': continue
        else: print("Opción inválida.")

    elif opcion == '2':
        convertir_temperatura()

    elif opcion == '3':
        print('¡Hasta luego!')
        break

    else:
        print('Opción inválida.')
