class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula", self.titulo)
        
    # Destructor de clase, este se ejecuta automaticamente para eliminar de memoria todas las instancias que existen
    def __del__(self):
        print("Se está borrando la pelicula", self.titulo)

p = Pelicula("El padrino",172,1972)
del(p)