class Pasajero:
    def __init__(self, nombre, nPas):
        self.nombre = nombre
        self.num_pasaporte = nPas #rellenar
        self.vReservado = []

    def datos_pasajero(self,nombre, num_vuelo):
        global r1
        r1= Reserva(nombre, num_vuelo, "aprobado") #activando el init

    def agregar_reservacion(self):
        r1.relleno_reserva()

    def cancelar_reservacion(self):
        r1.cancelar_reserva()

    def mostar_reservacion(self):
        return (p1.vReservado)

class Reserva:
    def __init__(self, pasaj, vuelo, estado):
        self.reservacion = [] #rellenar
        self.nPasajero = pasaj
        self.nVuelo = vuelo
        self.estado = estado

    def relleno_reserva(self):
        r1.reservacion.append([self.nPasajero, self.nVuelo, self.estado])
    
    def cancelar_reserva(self):
        r1.reservacion[0][2] = "cancelado"

    def mostrar_reserva(self):
        return (r1.reservacion)
    
class Avion(Pasajero, Reserva):
    def __init__(self, modelo, asientos):
        self.modelo = modelo
        self.num_asientos = asientos

class Vuelo(Pasajero, Reserva):
    def __init__(self, nVuelo, origen, destino, fecha, Aasig, modelo, asientos):
        a1 = Avion(modelo, asientos) #activando el init
        self.num_vuelo = nVuelo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.avion_asig = Aasig
        self.disponibilidad = a1.num_asientos
        self.cPasajero = []

    def toma_datos(self, clave_vuelo):
        global nombreP, num_pasaporteP,id_vuelo, p1
        nombreP = input("ingresar su nombre:  ")
        num_pasaporteP = input("ingresar su numero de pasaporte:  ")
        id_vuelo = clave_vuelo
        p1 = Pasajero(nombreP, num_pasaporteP) #activando el init
        v1.datos_pasajero(nombreP, id_vuelo)
    
    def most_vuelo_disp(self):
        if self.disponibilidad >= 1:
            return(f"num_vuelo: {self.num_vuelo}, origen: {self.origen}, destino: {self.destino}, fecha: {self.fecha[1]}, horario: {self.fecha[1]}, diponiblilidad de asientos: {self.disponibilidad}")
        else:
            return(f"el vuelo {self.num_vuelo}, con destino a {self.destino} no esta disponible")
    
    def agregar_vuelo(self):
        if self.disponibilidad >=1:
            if id_vuelo == self.num_vuelo and nombreP not in self.cPasajero:
                self.cPasajero.append(nombreP)
                p1.agregar_reservacion()
                p1.vReservado.append([id_vuelo, self.destino, self.fecha[0], self.fecha[1]])
                self.disponibilidad -=1

    def cancelar_vuelo(self):
        cancelar = input("quieres cancelar un vuelo: si o no   ")
        if cancelar == "si":
            if id_vuelo in p1.vReservado[0] and nombreP in self.cPasajero:
                self.cPasajero.remove(nombreP)
                p1.cancelar_reservacion()
                p1.vReservado = []
                self.disponibilidad +=1

    def mostar_reservacion(self):
        return (p1.vReservado)
    
    def lista_pasajero(self):
        return (self.cPasajero)

v1 = Vuelo("LA8131", "Santiago", "Sao Paulo", ("28 agosto", "18:00"), "Airbus 321", "Airbus 321", 220)
v2 = Vuelo("AM7550", "Santiago", "Buenos Aries", ("28 agosto", "21:45"), "737- 800", "737- 800", 160)
v3 = Vuelo("LA534", "Santiago", "Lima", ("29 agosto", "07:20"), "Boeing 787-8", "Bossseing 787-8", 247)

print(v1.most_vuelo_disp())
print(v2.most_vuelo_disp())
print(v3.most_vuelo_disp())

vuelo_buscado = input("ingresar el numero del vuelo que desea reservar:  ")

for usuario in(v1, v2, v3):
    if usuario.num_vuelo == vuelo_buscado:
        print("AGREGACION")
        usuario.toma_datos(vuelo_buscado)
        usuario.agregar_vuelo()

        print("lista de reservacion " + str(usuario.mostar_reservacion()))
        print("pasajero que hizo la reservacion " + str(usuario.mostrar_reserva()))
        print("lista de pasajeros del avion " + str(usuario.lista_pasajero()))

        print("CANCELACION")
        print("ahora vas a cancelar un vuelo")
        usuario.cancelar_vuelo()

        print("lista de reservacion " + str(usuario.mostar_reservacion()))
        print("pasajero que cancelo la reservacion " + str(usuario.mostrar_reserva()))
        print("lista de pasajeros del avion " + str(usuario.lista_pasajero()))