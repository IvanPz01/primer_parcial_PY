primera_cadena = input("Ingrese su primera cadena a comparar: ").lower()
segunda_cadena = input("Ingrese su segunda cadena a comparar: ").lower()


def comparar_cadenas_lexicograficas(primera_cadena,segunda_cadena):
    Cadena_resultado = 0
    cadena_resultado2 = 0
    for i in primera_cadena:
        acumulador = 0
        Cadena_resultado = acumulador + ord(i)

    for i in segunda_cadena:
        acumulador = 0
        cadena_resultado2 = acumulador + ord(i)

    if Cadena_resultado < cadena_resultado2:
        print('-1')
    
    if Cadena_resultado > cadena_resultado2:
        print('1')

    if Cadena_resultado == cadena_resultado2:
        print('0')

comparar_cadenas_lexicograficas(primera_cadena,segunda_cadena)