from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

productos_db = []


class Producto:

    def __init__(self, nombre: str, precio: float, stock: int):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def vender(self, cantidad: int):
        if cantidad > self.__stock:
            raise ValueError("Stock insuficiente")

        self.__stock -= cantidad

    def to_dict(self):
        return {
            "nombre": self.__nombre,
            "precio": self.__precio,
            "stock": self.__stock
        }



@app.route("/api/productos", methods=["GET"])
def listar_productos():

    lista = []

    for producto in productos_db:
        lista.append(producto.to_dict())

    return jsonify(lista), 200


@app.route("/api/productos", methods=["POST"])
def crear_producto():

    datos = request.json

    nombre = datos["nombre"]
    precio = datos["precio"]
    stock = datos["stock"]

    nuevo_producto = Producto(nombre, precio, stock)

    productos_db.append(nuevo_producto)

    return jsonify({"mensaje": "Producto creado correctamente"}), 201

if __name__ == "__main__":

    puerto = os.getenv("PORT", 5000)

    app.run(debug=True, port=puerto)