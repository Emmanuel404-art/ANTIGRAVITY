from flask import Blueprint, request, jsonify, Response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import db, Usuario

api_bp = Blueprint('api', __name__)

@api_bp.route('/usuarios/registrar', methods=['POST'])
def registrar_usuario() -> tuple[Response, int]:
    try:
        payload = request.get_json()

        clave_segura = generate_password_hash(payload['password'])

        return jsonify({"mensaje": "Usuario procesado"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@api_bp.route('/login', methods=['POST'])
def login() -> tuple[Response, int]:
    payload = request.get_json()

    usuario = Usuario.query.filter_by(
        username=payload.get('username')
    ).first()

    if usuario and check_password_hash(usuario.password_hash, payload.get('password')):

        identidad = {
            "username": usuario.username,
            "rol": usuario.rol
        }

        token_acceso = create_access_token(identity=identidad)

        return jsonify({
            "mensaje": "Login exitoso",
            "token": token_acceso
        }), 200

    return jsonify({"mensaje": "Credenciales inválidas"}), 401