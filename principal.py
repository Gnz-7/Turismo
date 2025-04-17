from Listas import lista_usuario,lista_atraccion,lista_promocion,lista_atraccion_promocion



    

resumen_dinero_restante = {}

for usuario in lista_usuario:
    
    plata = usuario.presupuesto
    tiempo = usuario.tiempo_disponible
    print("")
    print(usuario)
    
    while plata > 0:
        
        compra_realizada = False
        
        for atraccion in lista_atraccion:
                
            precio = atraccion.costo_visita
            duracion = atraccion.tiempo_duracion
                    
            if precio > plata or duracion > tiempo:
                continue
                
            print("------------------------------------------------------------------")
                
            print(f"{atraccion}")
            entrada = input("Desea comprar S/N: ").lower()
                
            if entrada == "s":
                plata -= precio
                tiempo -= duracion
                compra_realizada = True
                print(f"gastaste {precio}, te quedan {plata}")
                print(f"te consumio {duracion} horas, te quedan {tiempo}")
                
                if plata == 0 or tiempo == 0:
                    break
                
        if plata == 0 or tiempo == 0:
            break
        
        if not compra_realizada:
            print("---------------------------------------------------------------------")    
            print("SI NO TE INTERESA NINGUNO PUEDO OFRECERTE PROMOCIONES")
            print("---------------------------------------------------------------------")
        
        for promocion, costo_promocion in zip(lista_promocion, lista_atraccion_promocion):
                
            tipo = promocion.tipo
            suma_atracicones = costo_promocion.calcular_total_precio()
            calculo_AxB = costo_promocion.calcular_total_precio_AxB()
            valor = promocion.valor_descuento
        
            if suma_atracicones > plata:
                continue
                
            print(f"{promocion}")
            print(f"{suma_atracicones}")
            entrada = input("Desea comprar S/N: ").lower()
            print("------------------------------------------------------------------")
                
            if entrada == "s":
                    
                if tipo == "Por":
                    descuento = suma_atracicones * (valor / 100)
                    precio_final = suma_atracicones - descuento
                    plata -= precio_final
                        
                elif tipo == "Abs":
                    precio_final = suma_atracicones - valor
                    plata -= precio_final
                    
                elif tipo == "AxB":
                    precio_final = calculo_AxB
                    plata -= precio_final
                
                print(f"gastaste {precio_final}, te quedan {plata}")
                
                compra_realizada = True
                
                if plata == 0:
                    break
                
        if plata == 0:
            break
        
        if not compra_realizada:
            print("No realizaste ninguna compra, por lo que ya no se te ofrecerán más opciones.")
            break
    
    # Guardar dinero restante
    resumen_dinero_restante[usuario.nombre] = plata


# Mostrar resumen final
print("\n================== RESUMEN FINAL ==================")
for nombre, dinero in resumen_dinero_restante.items():
    print(f"{nombre} terminó con ${dinero:.2f}")