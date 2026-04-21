#calculo de volumen de objetos geometrico como cilindro, cono, esfera, ect
import math

#volumen de un cubo
def volumen_cubo(lado):
    return lado**3 

#volumen de un paralelepipedo
def volumen_paralelepipedo(largo, ancho, alto):
    return largo*ancho*alto

#volumen de un cubo hueco
def volumen_cubo_hueco(lado_externo, lado_interno):
    if lado_interno >= lado_externo:
        raise ValueError("El lado interno debe ser menor que el lado externo.")
    return lado_externo**3 - lado_interno**3

#volumen de un paralelepipedo hueco
def volumen_paralelepipedo_hueco(largo_externo, ancho_externo, alto_externo, largo_interno, ancho_interno, alto_interno):
    if (largo_interno >= largo_externo or 
        ancho_interno >= ancho_externo or 
        alto_interno >= alto_externo):
        raise ValueError("Las dimensiones internas deben ser menores que las externas.")
    volumen_externo = largo_externo * ancho_externo * alto_externo
    volumen_interno = largo_interno * ancho_interno * alto_interno
    return volumen_externo - volumen_interno

#volumen de un cilindro
def volumen_cilindro(radio, altura):
    return math.pi * radio**2 * altura

#volumen de un cilindro hueco
def volumen_cilindro_hueco(radio_externo, radio_interno, altura):
    if radio_interno >= radio_externo:
        raise ValueError("El radio interno debe ser menor que el radio externo.")
    return math.pi * (radio_externo**2 - radio_interno**2) * altura

#volumen de un cono
def volumen_cono(radio, altura):
    return (1/3) * math.pi * radio**2 * altura

#volumen de una esfera
def volumen_esfera(radio):
    return (4/3) * math.pi * radio**3

#volumen de una esfera hueca
def volumen_esfera_hueca(radio_externo, radio_interno):
    if radio_interno >= radio_externo:
        raise ValueError("El radio interno debe ser menor que el radio externo.")
    return (4/3) * math.pi * (radio_externo**3 - radio_interno**3)

#volumen de una piramide
def volumen_piramide(area_base, altura):
    return (1/3) * area_base * altura

#crear con whilw true el ciclo para que no se cierre el programa y se crean las opciones
while True:
    print("1. Calcular volumen de un cubo")
    print("2. Calcular volumen de un cubo hueco")
    print("3. Calcular volumen de un paralelepipedo")
    print("4. Calcular volumen de un paralelepipedo hueco")
    print("5. Calcular volumen de un cilindro")
    print("6. Calcular volumen de un cilindro hueco")
    print("7. Calcular volumen de un cono")
    print("8. Calcular volumen de una esfera")
    print("9. Calcular volumen de una esfera hueca")
    print("10. Calcular volumen de una piramide")
    print("11. Salir del programa")
    
    opcion = int(input("Indique la opción que desea usar: "))

    if opcion == 1:
        lado = float(input("Ingrese el lado del cubo (m): "))
        resultado = volumen_cubo(lado)
        print(f"El volumen del cubo es: {resultado:.2f} m³")

    elif opcion == 2:
        lado_externo = float(input("Ingrese el lado externo del cubo hueco (m): "))
        lado_interno = float(input("Ingrese el lado interno del cubo hueco (m): "))
        resultado = volumen_cubo_hueco(lado_externo, lado_interno)
        print(f"El volumen del cubo hueco es: {resultado:.2f} m³")
    
    elif opcion == 3:
        largo = float(input("Ingrese el largo del paralelepipedo (m): "))
        ancho = float(input("Ingrese el ancho del paralelepipedo (m): "))
        alto = float(input("Ingrese el alto del paralelepipedo (m): "))
        resultado = volumen_paralelepipedo(largo, ancho, alto)
        print(f"El volumen del paralelepipedo es: {resultado:.2f} m³") 

    elif opcion == 4:
        largo_externo = float(input("Ingrese el largo externo del paralelepipedo hueco (m): "))
        ancho_externo = float(input("Ingrese el ancho externo del paralelepipedo hueco (m): "))
        alto_externo = float(input("Ingrese el alto externo del paralelepipedo hueco (m): "))
        largo_interno = float(input("Ingrese el largo interno del paralelepipedo hueco (m): "))
        ancho_interno = float(input("Ingrese el ancho interno del paralelepipedo hueco (m): "))
        alto_interno = float(input("Ingrese el alto interno del paralelepipedo hueco (m): "))
        resultado = volumen_paralelepipedo_hueco(largo_externo, ancho_externo, alto_externo, largo_interno, ancho_interno, alto_interno)
        print(f"El volumen del paralelepipedo hueco es: {resultado:.2f} m³")

    elif opcion == 5:
        radio = float(input("Ingrese el radio del cilindro (m): "))
        altura = float(input("Ingrese la altura del cilindro (m): "))
        resultado = volumen_cilindro(radio, altura)
        print(f"El volumen del cilindro es: {resultado:.2f} m³")

    elif opcion == 6:
        radio_externo = float(input("Ingrese el radio externo del cilindro hueco (m): "))
        radio_interno = float(input("Ingrese el radio interno del cilindro hueco (m): "))
        altura = float(input("Ingrese la altura del cilindro hueco (m): "))
        resultado = volumen_cilindro_hueco(radio_externo, radio_interno, altura)
        print(f"El volumen del cilindro hueco es: {resultado:.2f} m³")

    elif opcion == 7:
        radio = float(input("Ingrese el radio del cono (m): "))
        altura = float(input("Ingrese la altura del cono (m): "))
        resultado = volumen_cono(radio, altura)
        print(f"El volumen del cono es: {resultado:.2f} m³")

    elif opcion == 8:
        radio = float(input("Ingrese el radio de la esfera (m): "))
        resultado = volumen_esfera(radio)
        print(f"El volumen de la esfera es: {resultado:.2f} m³")

    elif opcion == 9:
        radio_externo = float(input("Ingrese el radio externo de la esfera hueca (m): "))
        radio_interno = float(input("Ingrese el radio interno de la esfera hueca (m): "))
        resultado = volumen_esfera_hueca(radio_externo, radio_interno)
        print(f"El volumen de la esfera hueca es: {resultado:.2f} m³")

    elif opcion == 10:
        area_base = float(input("Ingrese el área de la base de la pirámide (m²): "))
        altura = float(input("Ingrese la altura de la pirámide (m): "))
        resultado = volumen_piramide(area_base, altura)
        print(f"El volumen de la pirámide es: {resultado:.2f} m³")

    elif opcion == 11:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
