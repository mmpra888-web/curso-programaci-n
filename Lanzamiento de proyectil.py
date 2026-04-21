#hoy vamos a lanzar un proyetil 
#vamos a nececitar la velocidad inicial y angulo de lanzamineto para el 1er caso
# vamos a calacular la altura maxima, el tiempo de vuelo y el alcanze del proyevtil 
# que pasa cuando me dan una de las 2 compotenentes de la velocidad inicial y el angulo de lanzamiento
# que sucede si el tenemos un odjetivos en cordenas x e y y queremos alcanzar el odjetivo con el proyetil 
# tambien si dedeamos impactar un odjetivo en movimiento con el proyetil como calcular el algulo y la velocidad inicial 
# y el movimiento del odjetivo va a ser en ambos caso mru o mruv

#se importan las librerias necesarias para el programa 
import math
#se define la gravedad
G=9.81
#se define la funcion para calcular la altura maxima del proyetil
def altura_max(vo,angulo,yo):
    #se convierte el angulo a radianes
    angulo_rad=math.radians(angulo)
    #se calcula la altura maxima con la formula h=vo^2*sin^2(angulo)/g
    h=yo+(vo**2)*(math.sin(angulo_rad)**2)/(G)
    return h

#se define la funcion para calcular el tiempo de vuelo del proyetil si la altura inicial es igual a la final
def tiempo_vuelo(vo,angulo):
    #se convierte el angulo a radianes
    angulo_rad=math.radians(angulo)
    #se calcula el tiempo de vuelo con la formula t=2*vo*sin(angulo)/g
    t=(2*vo*math.sin(angulo_rad))/G
    return t

#se define la funcion para calcular el tiempo de vuelo del proyetil si la altura inicial es diferente a la final
def tiempo_vuelo_altura(vo,angulo,yo):
    #se convierte el angulo a radianes
    angulo_rad=math.radians(angulo)
    #se calcula el tiempo de vuelo con la formula t=(vo*sin(angulo)+sqrt((vo*sin(angulo))^2+2*yo*g))/g
    t=(vo*math.sin(angulo_rad)+math.sqrt((vo*math.sin(angulo_rad))**2+2*yo*G))/G
    return t

#se define la funcion para calcular el alcanze del proyetil
def alcanze(vo,angulo):
    #se convierte el angulo a radianes
    angulo_rad=math.radians(angulo)
    #se calcula el alcanze con la formula R=vo^2*sin(2*angulo)/g
    R=(vo*math.cos(angulo_rad))*(vo)*math.sin(angulo_rad)/G
    return R

#se define la funcion para calcular el angulo de lanzamiento necesario para alcanzar un objetivo en coordenadas x e y
def calcular_angulos_proyectil(x, y, v0):
    """
    Calcula los dos posibles ángulos de lanzamiento para dar en un blanco.
    x: distancia horizontal (m)
    y: altura final relativa a la inicial (m)
    v0: velocidad inicial (m/s)
    g: gravedad (m/s^2)
    """
    
    # Coeficientes de la ecuación cuadrática para tan(theta)
    # (g*x^2 / (2*v0^2)) * tan^2(theta) - x * tan(theta) + (y + (g*x^2 / (2*v0^2))) = 0
    
    a = (G * x**2) / (2 * v0**2)
    b = -x
    c = y + a
    
    # Calcular el discriminante (b^2 - 4ac)
    discriminante = b**2 - 4 * a * c
    
    if discriminante < 0:
        return "El blanco está fuera de alcance con esa velocidad."
    
    # Resolver para tan(theta) usando la fórmula cuadrática
    tan_theta1 = (-b + math.sqrt(discriminante)) / (2 * a)
    tan_theta2 = (-b - math.sqrt(discriminante)) / (2 * a)
    
    # Convertir a grados
    angulo1 = math.degrees(math.atan(tan_theta1))
    angulo2 = math.degrees(math.atan(tan_theta2))
    
    return angulo1, angulo2

#se define la funcion para calcular el angulo de lanzamiento necesario para alcanzar un objetivo en movimiento con el proyetil
def calcular_angulo_proyectil_movil(x, y, v0, vx):
    """
    Calcula el ángulo de lanzamiento para dar en un blanco en movimiento.
    x: distancia horizontal al blanco (m)
    y: altura final relativa a la inicial (m)
    v0: velocidad inicial del proyectil (m/s)
    vx: velocidad horizontal del blanco (m/s)
    g: gravedad (m/s^2)
    """
    
    # El tiempo que tarda el proyectil en alcanzar la distancia x
    t = x / vx
    
    # La altura del proyectil en ese tiempo t debe ser igual a y
    # Usamos la fórmula de altura del proyectil: h(t) = v0*sin(theta)*t - (1/2)*g*t^2
    # Entonces, v0*sin(theta)*t - (1/2)*g*t^2 = y
    # Despejamos sin(theta): sin(theta) = (y + (1/2)*g*t^2) / (v0*t)
    
    sin_theta = (y + 0.5 * G * t**2) / (v0 * t)
    
    if sin_theta < -1 or sin_theta > 1:
        return "No es posible alcanzar el blanco con esa velocidad."
    
    angulo = math.degrees(math.asin(sin_theta))
    
    return angulo

#se crea con while true el ciclo para que no se cierre el programa y se crean las opciones
while True:   
    print("1. Calcular altura máxima, tiempo de vuelo y alcance del proyectil")
    print("2. Calcular ángulos de lanzamiento para alcanzar un objetivo en coordenadas x e y")
    print("3. Calcular ángulo de lanzamiento para alcanzar un objetivo en movimiento")
    print("4. Salir del programa")
    opcion = int(input("Indique la opción que desea usar: "))

    if opcion == 1:
        vo = float(input("Ingrese la velocidad inicial (m/s): "))
        angulo = float(input("Ingrese el ángulo de lanzamiento (grados): "))
        yo = float(input("Ingrese la altura inicial (m): "))
        
        h_max = altura_max(vo, angulo, yo)
        t_vuelo = tiempo_vuelo_altura(vo, angulo, yo)
        alcance_proyectil = alcanze(vo, angulo)
        
        print(f"Altura máxima: {h_max:.2f} m")
        print(f"Tiempo de vuelo: {t_vuelo:.2f} s")
        print(f"Alcance: {alcance_proyectil:.2f} m")

    elif opcion == 2:
        x = float(input("Ingrese la distancia horizontal al objetivo (m): "))
        y = float(input("Ingrese la altura final relativa a la inicial (m): "))
        v0 = float(input("Ingrese la velocidad inicial (m/s): "))
        
        angulos = calcular_angulos_proyectil(x, y, v0)
        if isinstance(angulos, str):
            print(angulos)
        else:
            print(f"Ángulos de lanzamiento posibles: {angulos[0]:.2f} grados y {angulos[1]:.2f} grados")

    elif opcion == 3:
        x = float(input("Ingrese la distancia horizontal al objetivo (m): "))
        y = float(input("Ingrese la altura final relativa a la inicial (m): "))
        v0 = float(input("Ingrese la velocidad inicial del proyectil (m/s): "))
        vx = float(input("Ingrese la velocidad horizontal del objetivo (m/s): "))
        
        angulo_movimiento = calcular_angulo_proyectil_movil(x, y, v0, vx)
        if isinstance(angulo_movimiento, str):
            print(angulo_movimiento)
        else:
            print(f"Ángulo de lanzamiento para alcanzar el objetivo en movimiento: {angulo_movimiento:.2f} grados")

    elif opcion == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, por favor indique una opción válida.")  
