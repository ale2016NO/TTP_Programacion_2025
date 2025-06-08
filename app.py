from flask import Flask, render_template, request, redirect, session
from flask import jsonify
import json
app = Flask(__name__)
app.secret_key = 'supersecret'

# --- FUNCIONES PARA MANEJAR EL ARCHIVO DE DATOS (data.json) ---

def load_data():
    try:
        with open('data.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Si el archivo no existe o está dañado, crea la estructura inicial
        return {
            "users": {
                "admin": {"password": "admin123", "role": "admin"},
                "viewer": {"password": "viewer123", "role": "viewer"}
            },
            "products": [
                {'id': 'P001', 'name': 'Laptop Gamer X', 'quantity': 12, 'price': 1450.00},
                {'id': 'P002', 'name': 'Monitor Curvo 27"', 'quantity': 25, 'price': 490.50},
                {'id': 'P003', 'name': 'Teclado Mecánico RGB', 'quantity': 50, 'price': 89.99}
            ],
            "sales_history": [
                {'productId': 'P001', 'date': '2024-01-07', 'unitsSold': 5},
                {'productId': 'P001', 'date': '2024-01-14', 'unitsSold': 7},
                {'productId': 'P001', 'date': '2024-01-21', 'unitsSold': 4},
                {'productId': 'P001', 'date': '2024-01-28', 'unitsSold': 8},
                {'productId': 'P002', 'date': '2024-01-07', 'unitsSold': 10},
                {'productId': 'P002', 'date': '2024-01-14', 'unitsSold': 12},
                {'productId': 'P002', 'date': '2024-01-14', 'unitsSold': 6},
                {'productId': 'P003', 'date': '2024-01-14', 'unitsSold': 12},
                {'productId': 'P003', 'date': '2024-01-14', 'unitsSold': 16}
                
            ]
        }

def save_data(data):
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

# --- CARGA LOS DATOS DEL ARCHIVO AL INICIAR LA APP ---
app_data = load_data()
users = app_data['users']
products = app_data['products']
sales_history = app_data['sales_history']


# --- RUTAS DE LA APLICACIÓN ---

@app.route('/')
def home():
    if 'user' in session:
        return redirect('/dashboard')
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user_data = users.get(username)

    if user_data and user_data['password'] == password:
        session['user'] = {'username': username, 'role': user_data['role']}
        return redirect('/dashboard')

    return render_template('login.html', error='Credenciales incorrectas')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    return render_template('dashboard.html', products=products)

@app.route('/add_product', methods=['POST'])
def add_product():
    if 'user' not in session or session['user']['role'] != 'admin':
        return redirect('/')

    # Lógica para generar un nuevo ID automáticamente
    max_id = 0
    if products:
        for p in products:
            num = int(p['id'][1:])
            if num > max_id:
                max_id = num
    new_id = f"P{max_id + 1:03d}"

    # Obtener datos del formulario
    name = request.form['name']
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])

    # Agregar el nuevo producto a la lista
    products.append({'id': new_id, 'name': name, 'quantity': quantity, 'price': price})

    # Guardar todos los datos en el archivo JSON
    save_data(app_data)

    return redirect('/dashboard')

@app.route('/api/sales-history/<product_id>')
def get_sales_history(product_id):
    if 'user' not in session:
        return jsonify({"error": "No autorizado"}), 401

    history_for_product = [sale for sale in sales_history if sale['productId'] == product_id]
    return jsonify(history_for_product)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)

