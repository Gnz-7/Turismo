class Usuario:
    
    def __init__(self, nombre, categoria_preferida, presupuesto,tiempo_disponible):
        self.nombre = nombre
        self.categoria_preferida = categoria_preferida
        self.presupuesto = presupuesto
        self.tiempo_disponible = tiempo_disponible
        
    def __str__(self):
        return f"{self.nombre}, {self.categoria_preferida}, {self.presupuesto}, {self.tiempo_disponible}"

#-----------------------------------------------------------------------------------------------    

class Atraccion:
    
    def __init__(self,nombre_atraccion,costo_visita,tiempo_duracion,cupo_atraccion,tipo_atraccion):
        
        self.nombre_atraccion = nombre_atraccion
        self.costo_visita = costo_visita
        self.tiempo_duracion = tiempo_duracion
        self.cupo_atraccion = cupo_atraccion
        self.tipo_atraccion = tipo_atraccion
        
    def __str__(self):
        return f"{self.nombre_atraccion}, {self.costo_visita}, {self.tiempo_duracion},{self.cupo_atraccion},{self.tipo_atraccion}"
    
#-----------------------------------------------------------------------------------------------   
    
class Promocion:
    
    def __init__(self, tipo, nombre_promo, categoria, atraccion1, atraccion2, atraccion_n, valor_descuento):
        self.tipo = tipo
        self.nombre_promo = nombre_promo
        self.categoria = categoria
        self.atraccion1 = atraccion1
        self.atraccion2 = atraccion2
        self.atraccion_n = atraccion_n
        self.valor_descuento = valor_descuento
        
    def __str__(self):
        return f"{self.tipo}, {self.nombre_promo}, {self.categoria}, {self.atraccion1}, {self.atraccion2}, {self.atraccion_n}, {self.valor_descuento}"
    
    
#-----------------------------------------------------------------------------------------------

class Atraccion_Promocion:
    
    def __init__(self, atraccion1, atraccion2, atraccion_n):
        self.atraccion1 = atraccion1
        self.atraccion2 = atraccion2
        self.atraccion_n = atraccion_n
        
    def calcular_total_precio(self):
        return self.atraccion1+self.atraccion2+self.atraccion_n
        
    def calcular_total_precio_AxB(self):
        self.atraccion_n = 0
        return self.atraccion1+self.atraccion2+self.atraccion_n
    

#-----------------------------------------------------------------------------------------------
