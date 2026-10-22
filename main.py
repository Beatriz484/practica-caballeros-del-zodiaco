# Caballeros del Zodiaco: práctica de clases y herencia en Python


class Guerrero:
    def __init__(self, nombre, cosmo, edad):
        self.nombre = nombre
        self.cosmo = cosmo
        self.edad = edad

    def mostrar_info(self):
      return f"Nombre: {self.nombre} | Cosmo: {self.cosmo} | Edad: {self.edad}"

class Caballero(Guerrero):
    def __init__(self, nombre, cosmo,edad,
                 armadura, constelacion):
        super().__init__(nombre, cosmo, edad) # reutiliza el __init__ del padre
        self.armadura = armadura
        self.costelacion = constelacion
    def equiparse(self):
        return f"{self.nombre} viste la armadura de {self.armadura}"

class Espectro(Guerrero):
    def __init__(self, nombre, cosmo,edad, sobrepelliz, estrella):
        super() .__init__(nombre,cosmo,edad)
        self.sobrepelliz = sobrepelliz
        self.estrella = estrella
    def mostrar_estrella(self):
        return f"{self.estrella} estrella"
    def mostrar_equiparse(self):
        return f"{self.sobrepelliz} equiparse"

class Dios(Guerrero):
    def __init__(self, nombre, cosmo, edad,reino,gobernar):
        self.reino = reino
        self.gobernar = gobernar
    def mostrar_reinos(self):
        return f"Reinos: {self.reino.mostrar_info()}"
    def mostrar_gobernar(self):
        return f"Gobernar: {self.reino.mostrar_info()}"

class CaballeroDeOro(Caballero):
    def __init__(self, nombre, cosmo,edad, casa, signo, septimosentido):
        self.casa = casa
        self.signo = signo
        self.septimosentido = septimosentido
    def mostrar_info(self):
        return (f"Casa: {self.casa.mostrar_info()}"
                f"signo: {self.signo}")
    def mostrar_septimosentido(self):
        return f"Septimosentido: {self.septimosentido}"
    def mostrar_casa_signo(self):
        return f"Casa: {self.casa.mostrar_info()}"
    def mostrar_casa_septimosentido_signo(self):
        return f"Casa: {self.casa.mostrar_info()}"

class CaballeroDeBronce(Caballero):
    def __init__(self, nombre, cosmo, edad, armadura, constelacion, maestro):
        super().__init__(nombre, cosmo, edad,armadura, constelacion)
        self.maestro = maestro
    def mostrar_info(self):
        return f"Caballero: {self.maestro}"
    def entrenar(self):
        return f"{self.nombre} entrena con {self.maestro}"

seiya = CaballeroDeBronce("Seiya", 100, 13, "Pegaso", "Pegaso", "Marin")
print(seiya.entrenar())
print(seiya.mostrar_info())










