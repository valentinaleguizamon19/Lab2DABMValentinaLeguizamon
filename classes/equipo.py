from ssl import OP_NO_RENEGOTIATION
from time import strftime
from tabulate import tabulate
from datetime import datetime
from datetime import timedelta

class Equipo:
    file ='c:/Users/valen/Downloads/DABM - VALENTINA LEGUIZAMON/T1/Lab2/database/Equipos.csv'
    def __init__(self,nombre,referencia,proveedor, cantidad,ciclo,fum=""):
        
        self.nombre = nombre
        self.referencia = referencia
        self.proveedor = proveedor
        self.ciclo = ciclo
        self.cantidad = cantidad
        self.fum = fum

    def verDatos(self):
        header = ["NOMBRE","REFERENCIA","PROVEEDOR","CANTIDAD","CICLO", "FUM"]
        datos = [[self.nombre,self.referencia,self.proveedor,self.cantidad, self.ciclo, self.fum]]
        print(tabulate(datos,header,tablefmt="grid"))
        return datos

    def save(self):
        file = open('c:/Users/valen/Downloads/DABM - VALENTINA LEGUIZAMON/T1/Lab2/database/Equipos.csv','a')
        linea = ";".join([self.nombre,self.referencia,self.proveedor,self.cantidad, self.ciclo, self.fum])
        file.write(linea+"\n")
        file.close()

def crearEquipo():

    print("REGISTRAR NUEVO EQUIPO")
    nombre = input("Nombre: ")
    referencia = input("Referencia: ")
    proveedor = input("Proveedor: ")
    cantidad = input("Cantidad: ")
    ciclo = input("Ciclo de mantenimiento (dias): ")
    fum = input("Fecha del último mantenimiento (yyyy/mm/dd): ",)

    e = Equipo(nombre,referencia, proveedor, cantidad, ciclo, fum)

    return e

def registroMantenimiento():

    print("REGISTRO ÚLTIMO MANTENIMIENTO")
    listaEquipos= getAllEquipos()
    equipo = input ("Equipo: ")
    fum = input("Fecha del último mantenimiento (yyyy/mm/dd): ")
    pos = 0
    
    for e in listaEquipos:
        if equipo in e:
            datosEquipo = e.split(";")
            datosEquipo[5] = fum + "\n"
            listaEquipos[pos] = ";".join(datosEquipo)
        pos = pos+1
    saveAllEquipos(listaEquipos)

def proxMantenimiento():
    print("REGISTRO PRÓXIMO MANTENIMIENTO")
    listaEquipos= getAllEquipos()
    datos = []

    for datosEquipo in listaEquipos:
        datosEquipo = datosEquipo.split(";")
        cant= int(datosEquipo[4])
        fum = datosEquipo[5].replace("\n","")
        fum = datetime.strptime(fum,'%Y/%m/%d')
        fpm = fum + timedelta(days=cant)
        datosEquipo.append(fpm)
        datos.append(datosEquipo)

    #RANGO DE FECHAS

    ci_fecha= input('Ingrese la fecha inicial "aaaa/mm/dd"... del rango que desea registrar')
    fecha_i =datetime.strptime(ci_fecha,'%Y/%m/%d')
    cf_fecha= input('Ingrese la fecha final "aaaa/mm/dd"... del rango que desea registrar')
    fecha_f =datetime.strptime(cf_fecha,'%Y/%m/%d')

    pos = 0
    disponibles = []

    for equipo in datos:
        dat = equipo[6]
        if dat >= fecha_i and dat <= fecha_f:
            disponibles.append(equipo)
    
    header = ["NOMBRE","REFERENCIA","PROVEEDOR","CANTIDAD","CICLO", "FUM","FPM"]
    print(tabulate(disponibles,header,tablefmt="grid"))
    
def disponibilidadEquipos():

    print("DISPONIBILIDAD DE EQUIPOS:")
    listaEquipos = getAllEquipos()
    equipo = input("Equipo: ")
    datos = []

    for e in listaEquipos:
        if equipo in e:
            e = e.split(';')
            cantidad = int(e[3])

            if cantidad == 0:
                print("No hay equipos disponibles")
            else:
                print ("La cantidad de equipos disponibles es:",cantidad)

def sumarCantidad(equip):
    listaEquipos = getAllEquipos()
    pos=0
    for eq in listaEquipos:
        if equip in eq:
            eq = eq.split(';')
            cantidad = int(eq[3])+1
            eq[3] = str(cantidad)
            listaEquipos[pos] = ";".join(eq)
        pos = pos+1
    saveAllEquipos(listaEquipos)

def restarCantidad(equip):
    print("LLEGUE HASTA ACA")
    listaEquipos = getAllEquipos()
    pos=0
    for eq in listaEquipos:
        if equip in eq:
            eq = eq.split(';')
            cantidad = int(eq[3])-1
            eq[3] = str(cantidad)
            listaEquipos[pos] = ";".join(eq)
        pos = pos+1
    saveAllEquipos(listaEquipos)

def saveAllEquipos(equipos):

    a = open('c:/Users/valen/Downloads/DABM - VALENTINA LEGUIZAMON/T1/Lab2/database/Equipos.csv','w')
    for e in equipos:
        a.write(e)
    a.close()

def getAllEquipos():
    a=open('c:/Users/valen/Downloads/DABM - VALENTINA LEGUIZAMON/T1/Lab2/database/Equipos.csv','r')
    datos = a.readlines()
    return datos
