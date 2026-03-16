from flask import Blueprint, request, jsonify, Response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import db, Usuario

api_bp = Blueprint('api', __name__)

@api_bp.route('/usuarios/registrar', methods=['POST'])
def registrar_usuario() -> tuple[Response, int]:
    try:
        payload = request.get_json()

        # 1. Hashing Criptográfico en RAM
        clave_segura = generate_password_hash(payload['password'])

        return jsonify({"mensaje": "Usuario procesado"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400