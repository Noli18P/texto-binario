def convertidor():
    diccionario_binario = {
        'A' : '01000001',
        'B' : '01000010',
        'C' : '01000011',
        'D' : '01000100',
        'E' : '01000101',
        'F' : '01000110',
        'G' : '01000111',
        'H' : '01001000',
        'I' : '01001001',
        'J' : '01001010',
        'K' : '01001011',
        'L' : '01001100',
        'M' : '01001101',
        'N' : '01001101',
        'Ñ' : '11010001',
        'O' : '01001111',
        'P' : '01010000',
        'Q' : '01010001',
        'R' : '01010010',
        'S' : '01010011',
        'T' : '01010100',
        'U' : '01010101',
        'V' : '01010110',
        'W' : '01010111',
        'X' : '01011000',
        'Y' : '01011001',
        'Z' : '01011010',
        '1' : '00110001',
        '2' : '00110010',
        '3' : '00110011',
        '4' : '00110100',
        '5' : '00110101',
        '6' : '00110110',
        '7' : '00110111',
        '8' : '00111000',
        '9' : '00111001',
        '0' : '00110000'
    }

    mensaje = input('Ingresa el mensaje: ').upper().replace(' ', '')
    mensaje = list(mensaje)

    mensaje_cifrado = ''
    for letra in mensaje:
        mensaje_cifrado += str(' ') + str(diccionario_binario.get(letra))

   
    return mensaje_cifrado


def bienvenida():
    mensaje_bienvenida = """
    Bienvenido al convertidor de texto a código binario,
    en el puedes usar números y letras (por ahora), solo 
    debes introducir una palabra o una oración entera si
    lo deseas. Disfrutalo!
    """

    print(mensaje_bienvenida)

def main():
    bienvenida()
    mensaje = convertidor()
    print(mensaje)

if __name__ == '__main__':
    main()