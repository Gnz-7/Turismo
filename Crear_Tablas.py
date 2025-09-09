from Conexion import comandosSqlCreate

CrearTablaUsuario = comandosSqlCreate("""CREATE TABLE IF NOT EXISTS USUARIO(
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    categoria_preferida TEXT NOT NULL,
    presupuesto FLOAT NOT NULL,
    tiempo_disponible INTEGER NOT NULL); """)

CrearTablaAtraccion = comandosSqlCreate("""CREATE TABLE IF NOT EXISTS ATRACCION(
    id_atraccion INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_atraccion TEXT NOT NULL,
    costo_visita FLOAT NOT NULL,
    tiempo_duracion INTEGER NOT NULL,
    cupo_atraccion INTEGER NOT NULL,
    tipo_atraccion TEXT NOT NULL); """)

CrearTablaPromocion = comandosSqlCreate("""CREATE TABLE IF NOT EXISTS PROMOCION(
    id_promocion INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL,
    nombre_promo TEXT NOT NULL,
    categoria TEXT NOT NULL,
    atraccion1 TEXT NOT NULL,
    atraccion2 TEXT NOT NULL,
    atraccion_n TEXT NOT NULL,
    valor_descuento INTEGER NOT NULL); """)



CrearTablaAtraccionPromocion = comandosSqlCreate("""CREATE TABLE IF NOT EXISTS ATRACCION_PROMOCION(
    id_promocion INTEGER NOT NULL,
    atraccion1 INTEGER NOT NULL,
    atraccion2 INTEGER NOT NULL,
    atraccion_n INTEGER NOT NULL,
    FOREIGN KEY (atraccion1) REFERENCES ATRACCION(id_atraccion),
    FOREIGN KEY (atraccion2) REFERENCES ATRACCION(id_atraccion),
    FOREIGN KEY (atraccion_n) REFERENCES ATRACCION(id_atraccion),
    FOREIGN KEY (id_promocion) REFERENCES PROMOCION(id_promocion)
); """)