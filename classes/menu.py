class Menu:
    
    def __init__(self,laboratorio):
        self.laboratorio = laboratorio
        
    def ver(self):
        print("BIENVENIDO AL SISTEMA".center(20,"*"))
        print("Laboratorio"+self.laboratorio)
        print("1.Técnicos")
        print("2.Estudiantes")

        op=input(">>>")

        return op

class MenuTecnicos():
    def ver(self):
        print("MENU TÉCNICOS DE LABORATORIO".center(20,"*"))
        print("1. Registrar equipos")
        print("2. Registrar prestamo")
        print("3. Registrar mantenimiento")
        print("4. Registrar entrega")
        print("5. Consultar próximos mantenimientos")
        print("6. S A L I R")

        op=input(">>>")
        return op

class MenuEstudiantes():
    def ver(self):
        print("MENU ESTUDIANTES".center(20,"*"))
        print("1. Consultar mis prestamos")
        print("2. Consultar disponibilidad de equipos")
        print("3. S A L I R")

        op=input(">>>")
        return op


if __name__=='__main__':
    m = Menu("Escuela de Ingeniería")
    m.ver()