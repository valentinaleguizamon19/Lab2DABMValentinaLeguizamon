'''Archivo principal - Laboratorio 2
Desarrollado por Valentina Leguizamón
'''
from classes.menu import *
from classes.equipo import *
from classes.prestamo import *

def main():
    menu = Menu(" Escuela de Ingeniería")
    op=menu.ver()

    if op == "1":
        menu2 = MenuTecnicos()
        op2 = menu2.ver()

        if op2 == "1":
            #Crear equipos
            e = crearEquipo()
            e.verDatos()
            e.save()

        elif op2 == "2":
            #Crear prestamos
            (p,equip) = crearPrestamo()
            p.verDatos()
            p.save()
            restarCantidad(equip)

        elif op2 == "3": 
            #Registrar mantenimientos
            registroMantenimiento()

        elif op2 == "4":
            #Registrar entregas
            equip = registroEntrega()
            sumarCantidad(equip)

        elif op2 == "5":
            #Consulta equipos por mantenimiento en un rango de fechas
            proxMantenimiento()

    elif op == "2":
        menu2 = MenuEstudiantes()
        op2 = menu2.ver()
    
        if op2 == "1":
            #Consulta de mis prestamos
            verPrestamo()

        elif op2 == "2":
            #Consulta de disponibilidad de equipos 
            disponibilidadEquipos()
    main()

if __name__=='__main__':
    main()
