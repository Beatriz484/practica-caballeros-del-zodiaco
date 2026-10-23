# Caballeros del Zodiaco: práctica de clases y herencia en Python
class Ataque:
    def __init__(self, nombre, herida):
        self.nombre = nombre
        self.herida = herida
    def mostrar_info(self):
        return f"Ataque: {self.nombre} {self.herida}"

class Guerrero:
    def __init__(self, nombre, cosmo, edad):
        self.nombre = nombre
        self.cosmo = cosmo
        self.edad = edad
        self.ataques = []

    def mostrar_info(self):
        return f"Nombre: {self.nombre} | Cosmo: {self.cosmo} | Edad: {self.edad}"

    def anadir_ataque(self, ataque):
        self.ataques.append(ataque)

    def mostrar_ataques(self):
        for ataque in self.ataques:
            print (ataque.mostrar_info())




class Caballero(Guerrero):
    def __init__(self, nombre, cosmo,edad, armadura, constelacion):
        super().__init__(nombre, cosmo, edad) # reutiliza el __init__ del padre
        self.armadura = armadura
        self.constelacion = constelacion

    def equiparse(self):
        return f"{self.nombre} viste la armadura de {self.armadura}"

class Espectro(Guerrero):
    def __init__(self, nombre, cosmo,edad, sobrepelliz, estrella):
        super() .__init__(nombre,cosmo,edad)
        self.sobrepelliz = sobrepelliz
        self.estrella = estrella
    def mostrar_estrella(self):
        return f"{self.estrella} estrella"

    def equiparse(self):
        return f"{self.nombre} viste la sobrepelliz de {self.sobrepelliz}"

class Dios(Guerrero):
    def __init__(self, nombre, cosmo, edad, reino):
        super().__init__(nombre, cosmo, edad)
        self.reino = reino
    def mostrar_reinos(self):
        return f"Reinos: {self.reino}"

    def gobernar(self):
        return f"{self.nombre} gobierna en {self.reino}"


class CaballeroDeOro(Caballero):
    def __init__(self, nombre, cosmo,edad, armadura, constelacion,
                 casa, signo,septimosentido):
        super().__init__(nombre, cosmo, edad, armadura, constelacion)  # reutiliza el __init__ del padre
        self.casa = casa
        self.signo = signo
        self.septimosentido = septimosentido
    def mostrar_info(self):
        return (f"Casa: {self.casa} | "
                f"Signo: {self.signo}")
    def mostrar_septimosentido(self):
        return f"Septimosentido: {self.septimosentido}"


class CaballeroDeBronce(Caballero):
    def __init__(self, nombre, cosmo, edad, armadura, constelacion, maestro):
        super().__init__(nombre, cosmo, edad,armadura, constelacion)
        self.maestro = maestro
    def mostrar_info(self):
        return f"Caballero: {self.maestro}"
    def entrenar(self):
        return f"{self.nombre} entrena con {self.maestro}"

# Personajes
#Caballeros de Bronce
seiya = CaballeroDeBronce(nombre = "Seiya", cosmo = 100, edad = 18, armadura = "Pegaso",
                          constelacion ="Pegaso", maestro = "Marin")
shiryu = CaballeroDeBronce(nombre="Shiryu", cosmo=95, edad=14,
                           armadura="Dragón", constelacion="Dragón",
                           maestro="Dohko")

hyoga = CaballeroDeBronce(nombre="Hyoga", cosmo=95, edad=14,
                          armadura="Cisne", constelacion="Cisne",
                          maestro="Camus")

shun = CaballeroDeBronce(nombre="Shun", cosmo=90, edad=13,
                         armadura="Andrómeda", constelacion="Andrómeda",
                         maestro="Albiore")

ikki = CaballeroDeBronce(nombre="Ikki", cosmo=110, edad=15,
                         armadura="Fénix", constelacion="Fénix",
                         maestro="Guilty")
# Espectro
radamanthys = Espectro(nombre="Radamanthys", cosmo=150, edad=30,
                       sobrepelliz="Wyvern",
                       estrella="Estrella Celeste de la Ferocidad")

minos = Espectro(nombre="Minos", cosmo=140, edad=28,
                 sobrepelliz="Grifo",
                 estrella="Estrella Celeste de la Nobleza")

eaco = Espectro(nombre="Éaco", cosmo=145, edad=29,
                sobrepelliz="Garuda",
                estrella="Estrella Celeste de la Violencia")
#Dios/a
hades = Dios(nombre="Hades", cosmo=500, edad=250, reino="Inframundo")
atenea = Dios(nombre="Atenea", cosmo=500, edad=13, reino="Santuario")

#Caballero de Oro
mu = CaballeroDeOro(nombre="Mu", cosmo=200, edad=20,
                    armadura="Aries", constelacion="Aries",
                    casa="Casa de Aries", signo="Aries",
                    septimosentido=True)
mascara_mortal = CaballeroDeOro(nombre="Máscara Mortal", cosmo=200, edad=26,
                                armadura="Cáncer", constelacion="Cáncer",
                                casa="Casa de Cáncer", signo="Cáncer",
                                septimosentido=True)
aioria = CaballeroDeOro(nombre="Aioria", cosmo=200, edad=24,
                        armadura="Leo", constelacion="Leo",
                        casa="Casa de Leo", signo="Leo",
                        septimosentido=True)
shaka = CaballeroDeOro(nombre="Shaka", cosmo=220, edad=20,
                       armadura="Virgo", constelacion="Virgo",
                       casa="Casa de Virgo", signo="Virgo",
                       septimosentido=True)
afrodita = CaballeroDeOro(nombre="Afrodita", cosmo=200, edad=20,
                          armadura="Piscis", constelacion="Piscis",
                          casa="Casa de Piscis", signo="Piscis",
                          septimosentido=True)

# Ataques
meteoros = Ataque(nombre="Meteoros de Pegaso", herida=25)
colera = Ataque(nombre="Cólera del Dragón", herida=28)
polvo = Ataque(nombre="Polvo de Diamantes", herida=26)
cadena = Ataque(nombre="Cadena Nebular", herida=22)
puno_fantasma = Ataque(nombre="Puño Fantasma", herida=30)
extincion = Ataque(nombre="Extinción Estelar", herida=40)
ondas = Ataque(nombre="Ondas Infernales", herida=35)
rayo_plasma = Ataque(nombre="Rayo de Plasma", herida=38)
tesoro = Ataque(nombre="Tesoro del Cielo", herida=45)
rosas = Ataque(nombre="Rosas Pirañas", herida=30)
gran_precaucion = Ataque(nombre="Gran Precaución", herida=42)
cosmo_marioneta = Ataque(nombre="Cosmo Marioneta", herida=36)
garuda = Ataque(nombre="Vuelo del Garuda", herida=37)

seiya.anadir_ataque(meteoros)
shiryu.anadir_ataque(colera)
hyoga.anadir_ataque(polvo)
shun.anadir_ataque(cadena)
ikki.anadir_ataque(puno_fantasma)
mu.anadir_ataque(extincion)
mascara_mortal.anadir_ataque(ondas)
aioria.anadir_ataque(rayo_plasma)
shaka.anadir_ataque(tesoro)
afrodita.anadir_ataque(rosas)
radamanthys.anadir_ataque(gran_precaucion)
minos.anadir_ataque(cosmo_marioneta)
eaco.anadir_ataque(garuda)

# Lista de guerreros
guerreros = [seiya, shiryu, hyoga, shun, ikki,
             mu, mascara_mortal, aioria, shaka, afrodita,
             radamanthys, minos, eaco, hades, atenea]

for guerrero in guerreros:
    print("---", guerrero.nombre, "---")
    print(guerrero.mostrar_info())
    guerrero.mostrar_ataques()
    print()