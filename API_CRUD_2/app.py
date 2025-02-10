from flask import Flask, request, jsonify

app = Flask(__name__)


electrodomesticos = {
    "refrigerador": {
        "marca": "Samsung",
        "modelo": "RT38K5930S8",
        "precio": 800,
        "capacidad_litros": 380,
        "consumo_energia": "A++",
    },
    "lavadora": {
        "marca": "LG",
        "modelo": "Turbodrum 15kg",
        "precio": 600,
        "capacidad_kg": 15,
        "tipo": "Carga superior",
    },
    "microondas": {
        "marca": "Panasonic",
        "modelo": "NN-SN966S",
        "precio": 200,
        "capacidad_litros": 45,
        "potencia_watts": 1250,
    },
    "televisor": {
        "marca": "Sony",
        "modelo": "Bravia X90J",
        "precio": 1200,
        "tamaño_pulgadas": 55,
        "resolucion": "4K UHD",
    },
    "aspiradora": {
        "marca": "Dyson",
        "modelo": "V15 Detect",
        "precio": 700,
        "tipo": "Inalámbrica",
        "potencia_watts": 230,
    },
}


@app.route('/')
def welcome():
    return '<h1>WELCOME TO FLASK</h1>'

@app.route('/products', methods=['GET'])
def get_products():
    if request.method == 'GET':
        return jsonify(electrodomesticos), 200
@app.route('/products', methods=['POST'])
def add_products():
    data = request.get_json()
    
    if not data or 'nombre' not in data:
        return jsonify({"error": "El campo 'nombre' es obligatori." }), 400
    
    nombre = data['nombre']
    
    if nombre in electrodomesticos:
        return jsonify({"Error": f"El producto '{nombre}' ya existe"}), 400
    
    electrodomesticos[nombre] = {
        "marca": data.get("marca", "Desconocida"),
        "modelo": data.get("modelo", "Sin modelo"),
        "precio": data.get("precio", 0),
    }
    
    return jsonify({"mensaje": f"Producto '{nombre}' agregado correctamente", "data": electrodomesticos[nombre]}), 201


@app.route('/products/<int:id>', methods=['PUT'])
def edit_product_by_id(id):
    if request.method == 'PUT':
        print()
    
    


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')