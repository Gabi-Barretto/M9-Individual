from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def insert_data():
    data = request.json
    valor = data['valor']
    conn = sqlite3.connect('Ponderada 5/src/dados.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO dados (valor) VALUES (?)", (valor,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Data inserted successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)

