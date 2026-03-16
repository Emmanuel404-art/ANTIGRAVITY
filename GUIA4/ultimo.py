from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.config["SECRET_KEY"] = "super-secret-key"
app.config["JWT_SECRET_KEY"] = "jwt-super-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)



class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(20), nullable=False)  # Admin u Operario

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Producto(db.Model):
    __tablename__ = "productos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)



def admin_required():
    claims = get_jwt()
    return claims.get("rol") == "Admin"


@app.route("/")
def home():
    return jsonify({"msg": "API funcionando"}), 200



@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data:
        return jsonify({"msg": "Faltan datos"}), 400

    username = data.get("username")
    password = data.get("password")
    rol = data.get("rol")

    if not username or not password or not rol:
        return jsonify({"msg": "username, password y rol son obligatorios"}), 400

    if rol not in ["Admin", "Operario"]:
        return jsonify({"msg": "Rol inválido (Admin u Operario)"}), 400

    if Usuario.query.filter_by(username=username).first():
        return jsonify({"msg": "Usuario ya existe"}), 400

    user = Usuario(username=username, rol=rol)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "Usuario creado"}), 201



@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"msg": "Faltan datos"}), 400

    username = data.get("username")
    password = data.get("password")

    user = Usuario.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({"msg": "Credenciales inválidas"}), 401

    access_token = create_access_token(
        identity=user.id,
        additional_claims={"rol": user.rol}
    )

    return jsonify({"access_token": access_token}), 200



@app.route("/productos", methods=["POST"])
@jwt_required()
def crear_producto():
    if not admin_required():
        return jsonify({"msg": "Acceso prohibido: requiere rol Admin"}), 403

    data = request.get_json()

    if not data:
        return jsonify({"msg": "Faltan datos"}), 400

    nombre = data.get("nombre")
    precio = data.get("precio")

    if not nombre or precio is None:
        return jsonify({"msg": "nombre y precio son obligatorios"}), 400

    producto = Producto(nombre=nombre, precio=precio)

    db.session.add(producto)
    db.session.commit()

    return jsonify({"msg": "Producto creado"}), 201



with app.app_context():
    db.create_all()
 

if __name__ == "__main__":
    app.run(debug=True)