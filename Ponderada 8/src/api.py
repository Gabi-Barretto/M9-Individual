from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

from dotenv import load_dotenv

load_dotenv() # Carrega variáveis de ambiente do arquivo .env

app = Flask(__name__)

# Replace 'your_connection_string' with your actual MongoDB connection string.
mongo_uri = os.getenv("MONGO_URL")
mongo_client = MongoClient(mongo_uri, tls=True, tlsAllowInvalidCertificates=True)


# Replace 'your_database' with your actual database name.
db = mongo_client['ponderada_8']

# Replace 'your_collection' with your actual collection name.
collection = db['ponderada_8']

@app.route('/data', methods=['POST'])
def insert_data():
    data = request.json
    valor = data['valor']

    # Insert data into MongoDB
    insert_result = collection.insert_one({"valor": valor})

    # You can use the insert_result to check if the insert was successful, etc.
    return jsonify({"message": "Data inserted successfully", "inserted_id": str(insert_result.inserted_id)}), 201

if __name__ == '__main__':
    app.run(debug=True)
