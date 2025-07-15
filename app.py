from flask import Flask, jsonify
import csv

app = Flask(__name__)

@app.route('/api/productos', methods=['GET'])
def obtener_productos():
    productos = {}
    with open('productos.csv', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            sku = fila.get('sku')
            if sku:
                productos[sku] = dict(fila)
    return jsonify(productos)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port)
