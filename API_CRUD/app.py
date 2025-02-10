from flask import Flask, request, jsonify

app = Flask(__name__)

customers_list = [
    {
    "id": 0,
    "name": "Juan Pérez",
    "email": "juan.perez@example.com",
    "phone": "555-1234"
    },
    {
    "id": 1,
    "name": "María García",
    "email": "maria.garcia@example.com",
    "phone": "555-5678"
    },
    {
    "id": 2,
    "name": "Carlos López",
    "email": "carlos.lopez@example.com",
    "phone": "555-9012"
    },
    {
    "id": 3,
    "name": "Ana Martínez",
    "email": "ana.martinez@example.com",
    "phone": "555-3456"
    }
]


@app.route('/')
def Welcome():
    return '<h1>Welcome</h1>'


@app.route('/customers',methods=['GET'])
def show_customers():
    if request.method == 'GET':
        return jsonify(customers_list)

@app.route('/customers',methods=['POST'])
def add_customers():
    if request.method == 'POST':
        
        data = request.get_json()
        
        if not data or not all(key in data for key in ["name", "email", "phone"]):
            return jsonify({"error": "Datos incompletos"}), 400
        
        new_id = customers_list[-1]["id"] + 1 if customers_list else 0
        
        new_customer = {
            "id": new_id,
            "name": data["name"],
            "email": data["email"],
            "phone": data["phone"]
        }
        
        customers_list.append(new_customer)
        
        return jsonify({"message": "Cliente agregado correctamente", "customer": new_customer}), 201

@app.route('/customers/<int:id>', methods=['GET'])
def get_customers_by_id(id):
    request.method == 'GET'
    
    return jsonify(customers_list[id])

@app.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    if request.method == 'PUT':
        
        data = request.get_json()
        
        if not data or not all(key in data for key in ["name", "email", "phone"]):
            return jsonify({"error": "Datos incompletos"}), 400
        
        # Buscar el cliente por su ID
        for customer in customers_list:
            if customer["id"] == id:
                # Actualizar los datos del cliente
                customer["name"] = data["name"]
                customer["email"] = data["email"]
                customer["phone"] = data["phone"]
                
                # Devolver una respuesta exitosa
                return jsonify({"message": "Cliente actualizado correctamente", "customer": customer}), 200
        
        # Si no se encuentra el cliente, devolver un error
        return jsonify({"error": "Cliente no encontrado"}), 404        



app.run(debug=True, port=5000, host='0.0.0.0')