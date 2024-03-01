import fitz
from flask import Flask, request, jsonify
from pprint import pprint

app = Flask(__name__)

@app.route('/authenticate', methods=['POST'])
def authenticate_and_show_metadata():
    auth_data = request.json
    username = auth_data.get('username')
    password = auth_data.get('password')
    if username == 'chirag' and password == 'chirag':
        return jsonify(show_metadata()), 200
    else:
        return jsonify({"message": "Authentication failed"}), 401

def show_metadata():
    doc1 = fitz.open(r"C:\Users\chira\Downloads\cv1.pdf")
    doc2 = fitz.open(r"C:\Users\chira\Downloads\cv1.pdf")
    metadata = {
        "doc1": doc1.metadata,
        "doc2": doc2.metadata
    }
    return metadata

if __name__ == '__main__':
    app.run(debug=True)