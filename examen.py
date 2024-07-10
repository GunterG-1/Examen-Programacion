import random 
import math 
trabajadores = ["Juan Pérez", "Maria Garcia", "Carlos López", "Ana Martínez", "Pedro Rodriguez", "Laura Hemández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"] 
sueldos = [] 
def asignar_sueldos_aleatorios(): 
    global sueldos 
    sueldos = [random.randint(300000, 2500000) for _ in range(10)] 
    print("Sueldos asignados aleatoriamente.") 
def clasificar_sueldos(): 
        bajos = []
        medios = [] 
        altos = [] 
        for i, sueldo in enumerate(sueldos):
             if sueldo < 800000: bajos.append((trabajadores[i], sueldo))
             elif sueldo <= 2000000: medios.append((trabajadores[i], sueldo)) 
             else: altos.append((trabajadores[i], sueldo)) 
             print("\nSueldos menores a $800.000")
             print("TOTAL:", len(bajos)) 
             for trabajador, sueldo in bajos:
                 print(trabajador, " - ", sueldo)
                 print("\nSueldos entre $800.000 y $2.000.000") 
                 print("TOTAL:", len(medios)) 
                 for trabajador, sueldo in medios: 
                    print(trabajador, " - ", sueldo)
                    print("\nSueldos superiores a $2.000.000") 
                    print("TOTAL:", len(altos))
                    for trabajador, sueldo in altos:
                         print(trabajador, " - ", sueldo)
                         total_sueldos = sum(sueldos) 
                         print("\nTOTAL SUELDOS: $", total_sueldos) 

def ver_estadisticas(): 
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos) 
    promedio = sum(sueldos) / len(sueldos) 
    media_geometrica = math.exp(sum(math.log(sueldo)
     for sueldo in sueldos) / len(sueldos)) 
    print("\nEstadísticas de Sueldos") 
    print("Sueldo más alto: $", sueldo_max) 
    print("Sueldo más bajo: $", sueldo_min) 
    print("Promedio de sueldos: $", promedio) 
    print("Media geométrica: $", media_geometrica) 

def reporte_sueldos(): 
        print("\nReporte de Sueldos") 
print("{:<20} {:<15} {:<15} {:<15} {:<15}".format('Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Líquido'))
for i, sueldo in enumerate(sueldos): 
    descuento_salud = sueldo * 0.07 
    descuento_afp = sueldo * 0.12 
    sueldo_liquido = sueldo - descuento_salud - descuento_afp 
    print("{:<20} {:<15} {:<15} {:<15} {:<15}".format(trabajadores[i], f"${sueldo}", f"${int(descuento_salud)}", f"${int(descuento_afp)}", f"${int(sueldo_liquido)}")) 

def main():
    while True: 
        print("\nMenú:") 
        print("1. Asignar sueldos aleatorios") 
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas") 
        print("4. Reporte de sueldos") 
        print("5. Salir del programa") 
        opcion = input("Seleccione una opción: ") 
        
        if opcion == "1": 
            asignar_sueldos_aleatorios()
        elif opcion == "2": 
            clasificar_sueldos()
        elif opcion == "3": 
            ver_estadisticas() 
        elif opcion == "4": 
            reporte_sueldos() 
        elif opcion == "5": 
            print("\nFinalizando programa..")
            print("Desarrollado por Gunter Garate") 
            print("RUT 21.667.060-4") 
            break 
    else: 
        print("Opción no válida. Intente nuevamente.") 
if __name__ == "__main__": 
    main()