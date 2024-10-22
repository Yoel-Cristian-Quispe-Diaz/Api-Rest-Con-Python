from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
import hashlib

# Configuración de la app
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # ¡Cambia esto!
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
jwt = JWTManager(app)



# Conexión a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestion_pacientes"
)

# Función auxiliar para hash MD5
def generate_md5_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de gestión de medica"}

# Registro de usuario
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"message": "Faltan campos requeridos"}), 400

    hashed_password = generate_md5_hash(data['password'])

    cursor = db.cursor()
    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(sql, (data['username'], hashed_password))
    db.commit()
    cursor.close()
    return jsonify({"message": "Usuario creado exitosamente"}), 201

# Inicio de sesión
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s", (data['username'],))
    user = cursor.fetchone()
    cursor.close()

    if user and user['password'] == generate_md5_hash(data['password']):
        access_token = create_access_token(identity=user['id'])
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Usuario o contraseña inválidos"}), 401

# Proteger rutas con JWT
@app.before_request
def before_request():
    if request.endpoint not in ['login', 'register']:
        jwt_required()(lambda: None)()


# Pacientes
@app.route('/pacientes', methods=['GET'])
def get_pacientes():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pacientes")
    pacientes = cursor.fetchall()
    cursor.close()
    
    return jsonify(pacientes)

@app.route('/pacientes', methods=['POST'])
def crear_paciente():
    data = request.get_json()
    cursor = db.cursor()
    sql = "INSERT INTO pacientes (nombre, apellido, fecha_nacimiento, direccion, telefono, correo) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (data['nombre'], data['apellido'], data['fecha_nacimiento'], data['direccion'], data['telefono'], data['correo'])
    cursor.execute(sql, values)
    db.commit()
    cursor.close()
    return jsonify({"mensaje": "Paciente creado exitosamente"}), 201

@app.route('/pacientes/<int:id>', methods=['GET'])
def obtener_paciente(id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pacientes WHERE id = %s", (id,))
    paciente = cursor.fetchone()
    cursor.close()
    return jsonify(paciente)

@app.route('/pacientes/<int:id>', methods=['PUT'])
def actualizar_paciente(id):
    data = request.get_json()
    cursor = db.cursor()
    sql = "UPDATE pacientes SET nombre=%s, apellido=%s, fecha_nacimiento=%s, direccion=%s, telefono=%s, correo=%s WHERE id=%s"
    values = (data['nombre'], data['apellido'], data['fecha_nacimiento'], data['direccion'], data['telefono'], data['correo'], id)
    cursor.execute(sql, values)
    db.commit()
    cursor.close()
    return jsonify({"mensaje": "Paciente actualizado exitosamente"})

@app.route('/pacientes/<int:id>', methods=['DELETE'])
def eliminar_paciente(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM pacientes WHERE id = %s", (id,))
    db.commit()
    cursor.close()
    return jsonify({"mensaje": "Paciente eliminado exitosamente"})

# Gestión de citas
@app.route('/citas', methods=['GET'])
def obtener_citas():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM citas")
    citas = cursor.fetchall()
    cursor.close()
    return jsonify(citas)

@app.route('/citas', methods=['POST'])
def crear_cita():
    data = request.get_json()
    cursor = db.cursor()
    sql = "INSERT INTO citas (paciente_id, medico_id, fecha_hora, motivo, estado) VALUES (%s, %s, %s, %s, %s)"
    values = (data['paciente_id'], data['medico_id'], data['fecha_hora'], data['motivo'], data['estado'])
    cursor.execute(sql, values)
    db.commit()
    cursor.close()
    return jsonify({"mensaje": "Cita creada exitosamente"}), 201

@app.route('/citas/<int:id>', methods=['GET'])
def obtener_cita(id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM citas WHERE id = %s", (id,))
    cita = cursor.fetchone()
    cursor.close()
    return jsonify(cita)

@app.route('/citas/<int:id>', methods=['PUT'])
def actualizar_cita(id):
    data = request.get_json()
    cursor = db.cursor()
    sql = "UPDATE citas SET paciente_id=%s, medico_id=%s, fecha_hora=%s, motivo=%s, estado=%s WHERE id=%s"
    values = (data['paciente_id'], data['medico_id'], data['fecha_hora'], data['motivo'], data['estado'], id)
    cursor.execute(sql, values)
    db.commit()
    cursor.close()
    return jsonify({"mensaje": "Cita actualizada exitosamente"})

@app.route('/citas/<int:id>', methods=['DELETE'])
def eliminar_cita(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM citas WHERE id = %s", (id,))
    db.commit()
    cursor.close()
    return jsonify({"mensaje": "Cita eliminada exitosamente"})

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True)