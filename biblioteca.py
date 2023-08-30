#0. LISTO Deberás crear clases para representar libros, usuarios, préstamos y el catálogo de la biblioteca.
#0. LISTO El sistema permitirá: 
#1. LISTO  Añadir y eliminar libros al catálogo.
#2. LISTO  PARCIALMENTE Registrar usuarios.
#3. LISTO  Prestar y devolver libros. 
#4. LISTO  Consultar libros disponibles. 
#5. LISTO  Ver el historial de préstamos de un usuario

#usted define las funcionalidades

class Libro:
    def __init__(self, autor, nombre):
        self.autor = autor
        self.nombreL = nombre

    def __str__(self):
        return (f"nombre autor {self.autor}, nombre libro {self.nombreL}")

class Catalogo:
    def __init__(self):
        self.catalogo = {} #almacena todos los libros

    def agregarLibro(self, autor, nombre):
        self.c1.catalogo[autor] = {nombre:"disponible"}

    def eliminarLibro(self, autor, nombre):
        key = list(self.c1.catalogo[autor]) #el diccionario lo paso a lista
        if nombre == key[0]:
            self.c1.catalogo[autor][nombre] = "no disponible"
    
    def libroDisponible(self, autor, nombre):
        if self.c1.catalogo[autor][nombre] == "disponible":
            print(f"el libro {nombre} se encuentra disponible, por lo que temporalmente es tuyo")
            return 1

    def mostrarCatalogo(self):
        print(self.c1.catalogo)

class Prestamo(Catalogo):
    def __init__(self):
        self.historial = {}
        self.contador = 1

    def prestarLibro(self, autor, nombre):
        if self.libroDisponible(autor, nombre) == 1:
            self.p1.historialUsuario(autor, nombre)
            self.c1.catalogo[autor][nombre] = "no disponible"
        else:
            print("libro no disponible")

    def devolverLibro(self, autor, nombre):
        key = list(self.c1.catalogo[autor]) #el diccionario lo paso a lista
        if key[0] == nombre:
            self.c1.catalogo[autor][nombre] = "disponible"

    def historialUsuario(self, autor, nombre):
        self.historial[self.contador] = {autor:nombre}
        self.contador +=1

    def verHistorial(self):
        print(self.p1.historial)
        
class Usuario(Prestamo):
    def __init__(self):
        pass
    def conexionCatalogo(self):
        global c1
        self.c1 = Catalogo()

    def conexionLibro(self, nombre, autor):
        global l1
        self.l1 = Libro(nombre, autor)

    def conexionPrestamo(self):
        global p1
        self.p1 = Prestamo()

    def registarUsuario(self):
        nombre = input("ingresar su nombre de usuario:  ")
        self.conexionPrestamo() #instancio la clase Prestamo 

L1 = Libro("agatha christie", "muerte en el nilo")
L2 = Libro("antoine de saint-exupéry", "el principito")

#print(str(L1) + "\n" + str(L2))

u1 = Usuario()

u1.registarUsuario()

u1.conexionCatalogo()
u1.conexionPrestamo()

u1.agregarLibro("agatha christie", "muerte en el nilo")
u1.agregarLibro("antoine de saint-exupéry", "el principito")

u1.mostrarCatalogo()

u1.eliminarLibro("antoine de saint-exupéry", "el principito")
u1.mostrarCatalogo()

u1.prestarLibro(input("nombre del autor:  "), input("nombre del libro:  "))
#u1.prestarLibro(input("nombre del autor:  "), input("nombre del libro:  "))

u1.verHistorial()
u1.mostrarCatalogo()

input("presionar ENTER para devolver el libro")

u1.devolverLibro("agatha christie", "muerte en el nilo")
#u1.devolverLibro("antoine de saint-exupéry", "el principito")
u1.mostrarCatalogo()