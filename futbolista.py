from deportista import Deportista
class Futbolista(Deportista):
    listaFutbolistas = list()
    def __init__(self,nombre,edad,altura,sexo,añosPracticando,golesMarcados,tarjetasRojas,piernaHabil):
        super().__init__(nombre,edad,altura,sexo,"Futbol",añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)

    @classmethod
    def setListaFutbolista(clc,listaFutbolistas):
        clc.listaFutbolistas = listaFutbolistas
        
    @classmethod
    def getListaFutbolista(clc):
        return clc.listaFutbolistas
    
    def getGolesMarcados(self):
        return self._golesMarcados

    def setGolesMarcados(self,golesMarcados):
        self._golesMarcados = golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def setTarjetasRojas(self,tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil

    def setPiernaHabil(self,piernaHabil):
        self._piernaHabil = piernaHabil

    def __str__(self)->str:
        return (f"Mi nombre es {self.getNombre()} soy profesional en el deporte Futbol Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte")