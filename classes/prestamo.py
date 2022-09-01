from tabulate import tabulate

class prestamo:
    file ='c:/Users/valen/Downloads/DABM - VALENTINA LEGUIZAMON/T1/Lab2/database/Prestamos.csv'

    def __init__(self,nombre,carnet,equipo,fechaPrestamo,fechaEntrega):
        
        self.nombre = nombre
        self.carnet = carnet
        self.equipo = equipo
        self.fechaPrestamo = fechaPrestamo
        self.fechaEntrega = fechaEntrega

    def verDatos(self):
        header = ["NOMBRE","CARNET","EQUIPO","FECHA DE PRESTAMO","FECHA DE ENTREGA"]
        datos = [[self.nombre,self.carnet,self.equipo,self.fechaPrestamo, self.fechaEntrega]]
        print(tabulate(datos,header,tablefmt="grid"))
        return datos

    def save(self):
        file = open('c:/Users/valen/Downloads/DABM - VALENTINA LEGUIZAMON/T1/Lab2/database/Prestamos.csv','a')
        linea = ";".join([self.nombre,self.carnet,self.equipo,self.fechaPrestamo, self.fechaEntrega])
        file.write(linea+"\n")
        file.close()
    
def crearPrestamo():

    print("REGISTRAR PRESTAMO")
    nombre = input("Nombre: ")
    carnet = input("Carnet: ")
    equipo = input("Equipo: ")
    fechaPrestamo = input("Fecha de prestamo (yyyy-mm-dd): ")
    fechaEntrega = input("Fecha de entrega (yyyy-mm-dd): ")
    equip = equipo

    p = prestamo(nombre,carnet, equipo, fechaPrestamo, fechaEntrega)

    return (p, equip)

def verPrestamo():
    print("CONSULTA DE PRESTAMOS")
    listaPrestamos = getAllPrestamos()

    carnet = input("Carnet: ")
    datos = []

    for e in listaPrestamos:
        if carnet in e:
            e = e.split(';')
            datos.append(e)
            
    header = ["NOMBRE","CARNET","EQUIPO","FECHA DE PRESTAMO","FECHA DE ENTREGA"]
    print(tabulate(datos,header,tablefmt="grid"))

def getAllPrestamos():
    p = open('c:/Users/valen/Downloads/DABM - VALENTINA LEGUIZAMON/T1/Lab2/database/Prestamos.csv','r')
    prest = p.readlines()
    return prest

def saveAllPrestamos(prestamos):
    p = open('c:/Users/valen/Downloads/DABM - VALENTINA LEGUIZAMON/T1/Lab2/database/Prestamos.csv','w')
    for e in prestamos:
        p.write(e)
    p.close()

def registroEntrega():
    #LA IDEA ES BORRAR DE LA LISTA DE PRESTAMO
    print("REGISTRO ENTREGA")
    listaPrestamos= getAllPrestamos()
    
    carnet = input("Carnet: ")
    equip = input ("Equipo: ")
    
    pos = 0
    
    for e in listaPrestamos:
        if equip in e and carnet in e:
            listaPrestamos.pop(pos)
        pos = pos+1

    saveAllPrestamos(listaPrestamos)
    return(equip)