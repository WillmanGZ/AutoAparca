import mysql.connector

conexion_usuarios = mysql.connector.connect(
  host="localhost",
  user="Willman",
  password="Willman0520.",
  database="usuarios"
)

cursor = conexion_usuarios.cursor()
crear_tabla_sql = """
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(255) NOT NULL,
    contraseña VARCHAR(255) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    cedula VARCHAR(255) NOT NULL,
    telefono VARCHAR(255) NOT NULL
)
"""

# Ejecutar el comando
cursor.execute(crear_tabla_sql)

# Guardar los cambios
conexion_usuarios.commit()

# Cerrar el cursor y la conexión
cursor.close()
conexion_usuarios.close()

def insertar_usuario(conexion, usuario, contraseña, nombre, cedula, telefono):
    cursor = conexion.cursor()
    query = "INSERT INTO usuarios (usuario, contraseña, nombre, cedula, telefono) VALUES (%s, %s, %s, %s, %s)"
    valores = (usuario, contraseña, nombre, cedula, telefono)
    
    try:
        cursor.execute(query, valores)
        conexion.commit()
        print("Usuario insertado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def consultar_usuarios(conexion):
    cursor = conexion.cursor()
    query = "SELECT usuario, nombre, cedula, telefono FROM usuarios"
    
    try:
        cursor.execute(query)
        for (usuario, nombre, cedula, telefono) in cursor:
            print(f"Usuario: {usuario}, Nombre: {nombre}, Cédula: {cedula}, Teléfono: {telefono}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        
def verificar_usuario_contrasena(conexion_usuarios, usuario, contrasena):
    cursor = conexion_usuarios.cursor()
    query = "SELECT COUNT(*) FROM usuarios WHERE usuario = %s AND contraseña = %s"
    valores = (usuario, contrasena)
    
    try:
        cursor.execute(query, valores)
        resultado = cursor.fetchone()  # Obtener el primer resultado
        
        if resultado and resultado[0] > 0:
            return True  # Usuario y contraseña correctos
        else:
            return False  # Usuario o contraseña incorrectos
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False  # En caso de error, retornar False
    finally:
        cursor.close()
