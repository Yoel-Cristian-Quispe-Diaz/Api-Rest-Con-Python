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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000, debug=True)


