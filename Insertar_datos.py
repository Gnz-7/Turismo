from Conexion import comandosSql

# with open('./usuario.csv', 'r', encoding='utf-8') as file:
#    for line in file.readlines():
#        texto = f'''
#            INSERT INTO USUARIO (nombre, categoria_preferida, presupuesto, tiempo_disponible)
#            VALUES ('{line.split(',')[0]}', '{line.split(',')[1]}', '{line.split(',')[2]}', '{line.split(',')[3]}')
#        '''

#        comandosSql(texto)



# with open('./atraccion.csv', 'r', encoding='utf-8') as file:
#    for line in file.readlines():
#        texto = f'''
#            INSERT INTO ATRACCION (nombre_atraccion,costo_visita,tiempo_duracion,cupo_atraccion,tipo_atraccion)
#            VALUES ('{line.split(',')[0]}', '{line.split(',')[1]}', '{line.split(',')[2]}', '{line.split(',')[3]}', '{line.split(',')[4]}')
#        '''
       
       
#        comandosSql(texto)
       

# with open('./promocion.csv', 'r', encoding='utf-8') as file:
#    for line in file.readlines():
#        texto = f'''
#            INSERT INTO PROMOCION (tipo,nombre_promo,categoria,atraccion1,atraccion2,atraccion_N,valor_descuento)
#            VALUES ('{line.split(',')[0]}', '{line.split(',')[1]}', '{line.split(',')[2]}', '{line.split(',')[3]}', '{line.split(',')[4]}','{line.split(',')[5]}','{line.split(',')[6]}')
#        '''
       
#        comandosSql(texto)




# with open("./atraccion_promocion.csv", "r", encoding="UTF-8") as file:
    
#     for line in file.readlines():
#         texto = f'''
#            INSERT INTO ATRACCION_PROMOCION (id_promocion, atraccion1, atraccion2, atraccion_n)
#            VALUES ('{line.split(',')[0]}', '{line.split(',')[1]}', '{line.split(',')[2]}', '{line.split(',')[3]}')
#            '''
        
#         comandosSql(texto)