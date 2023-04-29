class Equipo:
   def __init__(self,logotipo, jugadores, dir_tecnico,nombre):
        self.logotipo = logotipo
        self.jugadores  = jugadores
        self.dir_tecnico = dir_tecnico
        self.nombre = nombre

   def agregar_jugador(self,jugador):
    self.jugadores.append(jugador)

class Jugador:
   def __init__(self,nombre, numero, nacionalidad,posicion,rol):
        self.nombre = nombre
        self.numero = numero
        self.nacionalidad = nacionalidad
        self.posicion = posicion
        self.rol = rol

class Torneo:
   def __init__(self,equipo, partidos,fechas):
        self.equipo = equipo
        self.partidos = partidos
        self.fechas = fechas

   def agregar_partido(self, equipo1, equipo2, estadio, fecha):
        partido = Partido(equipo1, equipo2, estadio, fecha)
        self.partidos.append(partido)

   def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

   def mostrar_partidos(self):
        for partido in self.torneo.partidos:
            print(partido.equipo1.nombre, "vs", partido.equipo2.nombre, "en", partido.estadio, "el", partido.fecha)


class DirectorTecnico:
    def __init__(self, nombre, nacionalidad, porcentaje):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.porcentaje = porcentaje
    
    def agregar_director_tecnico(self, director_tecnico):
        self.agregar_director_tecnico.append(director_tecnico)

class TablaPosiciones:
   def __init__(self,torneo, equipos_torneo):
        self.torneo = torneo
        self.equipos_torneo = equipos_torneo


   def agregar_goles(self, goles):
        self.goles += goles

   def agregar_puntos(self, puntos):
        self.puntos += puntos

   def agregar_partido_ganado(self):
        self.partidos_ganados += 1

   def agregar_partido_empatado(self):
        self.partidos_empatados += 1

   def agregar_partido_perdido(self):
        self.partidos_perdidos += 1
   
            

class EquipoTorneo:
   def __init__(self,equipo,goles, puntos, partidos_ganados,partidos_empatados,partidos_perdidos):
        self.equipo = equipo
        self.goles = goles
        self.puntos = puntos
        self.partidos_ganados = partidos_ganados
        self.partidos_empatados = partidos_empatados
        self.partidos_perdidos = partidos_perdidos
  
  
   def mostrar_equipos(self):
        for equipo in self.equipos:
            print(equipo.nombre)
    

class Partido:
   def __init__(self,equipo1, equipo2, estadio,fecha):
        self.equipo1 = equipo1
        self.equipo2= equipo2
        self.estadio = estadio
        self.fecha = fecha

   def mostrar_partido(self):
          return f"{self.equipo1} vs {self.equipo2} en {self.estadio} el {self.fecha}"
   
 
class Resultado:
   def __init__(self,partido, goles_e1,goles_e2):
        self.partido = partido
        self.goles_e1 = goles_e1
        self.goles_e2 = goles_e2

   def obtener_resultado_completo(self):
        equipo1 = self.partido[0]
        equipo2 = self.partido[1]
        estadio = self.partido[2]
        fecha = self.partido[3]
        return f"{equipo1} {self.goles_e1} - {self.goles_e2} {equipo2}, {estadio}, {fecha}"