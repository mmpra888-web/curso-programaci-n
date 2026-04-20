#colocar nombre del progama
print("***NOTAS DEL EXAMEN***")
#PERGUTAR LA MATERIA, EL PROFERSOR Y CUAL TIPO DE EVALUCION ES
estudiantes=[]
materia=input("¿Cuál es la materia ? ")
profe=input("¿Quien es el profesor? ")
evaluacion=input("¿Qué tipo de evalucion es? (Parcial, quiz, tarea, ... ect)")

#con while true comienzo el ciclo para que no se cierre el programa y creo las opciones
#1 resgistrar estudiante con su nota y ci 2 mostrar las notas registrada 3 calacuar el promedio de la seccio y 4 salir del programa
while True:
    print("1. Registrar estudiantes y su nota")
    print("2. Moatrar las notas registrads de la materia")
    print("3, calcular nota promedio de la evaluacion")
    print("4. salir del programa")
    opcion=int(input("Indique la opccion que desea usar: "))

    if opcion==1:
        #indico que se va a registras un nuevo estudinte y pido sus datos
        print("***REGISTRAR UN NUEVO ESTUDIANTE***")
        print("recuerde usar Nombres y apellidos compeltos sin abrevieturas")
        print()
        nombre=input("Indique nombre del estudiante: ")
        apellido=input("Indique apellido del estudiante: ")
        ci=input("Indique el numero de cedula del estudiente: ")
        nota=float(input("Indique la nota del estudiate "))

        #creamaos la verificaion de que ningun dato este vacio y la nota no sea menor a o mayor a 20 puntos
        if nombre=="" or apellido=="" or ci=="" :
            print("Recuerde llenar todos los datos del estudiante")
        elif nota<0 or nota>20:
            print("La nota debe estar entre 0 y 20 puntos")
        else:
        #registrar en una biblioteca todos los datos del estudiante
            estudiante={
                "nombre": nombre, 
                "apellido": apellido, 
                "ci": ci, 
                "nota": nota}
            estudiantes.append(estudiante)
            print("Estudinate registrado")
        
    elif opcion==2:
        print("***NOTAS REGISTRADAS DE LA MATERIA***")
        if len(estudiantes)==0:
            print("No hay estudiantes registrados para esta materia")
        else:
            for estudiante in estudiantes:
                print(f"Nombre: {estudiante['nombre']} {estudiante['apellido']}, CI: {estudiante['ci']}, Nota: {estudiante['nota']}")

    elif opcion==3:
        print("***NOTA PROMEDIO DE LA EVALUACION***")
        if len(estudiantes)==0:
            print("No hay estudiantes registrados para esta materia")
        else:
            total_notas=0
            for estudiante in estudiantes:
                total_notas+=estudiante["nota"]
            promedio=total_notas/len(estudiantes)
            print(f"La nota promedio de la evaluacion es: {promedio:.2f}")

    elif opcion==4:
        print("gracias por usar el programa")
        break
    else:
        print("Opcion invalidada, por favor indique una opcion valida")

