from Clases import Usuario, Atraccion, Promocion, Atraccion_Promocion
from Conexion import comandosSql


#--------------------------------------------------------------------------------------------------------------

usuario = comandosSql("SELECT nombre, categoria_preferida, presupuesto, tiempo_disponible FROM USUARIO")

lista_usuario = []

for i in usuario:
    lista_usuario.append(Usuario(i[0],i[1],i[2],i[3]))

#---------------------------------------------------------------------------------------------------------------

lista_atraccion = []

atraccion = comandosSql("SELECT nombre_atraccion,costo_visita,tiempo_duracion,cupo_atraccion,tipo_atraccion FROM ATRACCION")

for i in atraccion:
    lista_atraccion.append(Atraccion(i[0],i[1],i[2],i[3],i[4]))

#---------------------------------------------------------------------------------------------------------------


lista_promocion = []

promocion = comandosSql("SELECT tipo, nombre_promo, categoria, atraccion1, atraccion2, atraccion_n, valor_descuento FROM PROMOCION")

for i in promocion:
    lista_promocion.append(Promocion(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))

#--------------------------------------------------------------------------------------------------------------

lista_atraccion_promocion = []

cuenta = comandosSql("""SELECT 
    COALESCE(a1.costo_visita, 0) AS costo_atraccion1, 
    COALESCE(a2.costo_visita, 0) AS costo_atraccion2,
    COALESCE(an.costo_visita, 0) AS costo_atraccion_n
FROM ATRACCION_PROMOCION ap
LEFT JOIN ATRACCION a1 ON a1.id_atraccion = ap.atraccion1
LEFT JOIN ATRACCION a2 ON a2.id_atraccion = ap.atraccion2
LEFT JOIN ATRACCION an ON an.id_atraccion = ap.atraccion_n;""")

for i in cuenta:
    lista_atraccion_promocion.append(Atraccion_Promocion(i[0],i[1],i[2]))

