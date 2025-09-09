import sqlite3

# Función para ejecutar comandos SQL que crean o alteran tablas
def comandosSqlCreate(sql):
    con = sqlite3.connect('Divercion.db')
    cur = con.cursor()    
    data_sql = cur.execute(sql)
    con.commit()
    con.close()
    return data_sql

# Función para ejecutar comandos SQL
def comandosSql(sql):
    con = sqlite3.connect('Divercion.db')
    cur = con.cursor()
    data_sql = cur.execute(sql)
    data = data_sql.fetchall()
    con.commit()
    con.close()
    return data