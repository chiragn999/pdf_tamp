import PyPDF2
import re
import datetime
from flask import Flask, request, jsonify

def convert_pdf_date_string(pdf_date_string):
    # Convert PDF date string to a Python datetime object
    match = re.match(r"D:(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})([Z|+|-]\d{2}'\d{2}')", pdf_date_string)
    if match:
        groups = match.groups()
        return datetime.datetime(*map(int, groups))
    return None

def get_pdf_metadata(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfFileReader(file)

            # Get document info
            document_info = pdf_reader.getDocumentInfo()

            # Get creation and modification dates
            created_date = document_info.get('/CreationDate')
            modified_date = document_info.get('/ModDate')

            # Convert timestamp to a human-readable format
            created_date_str = convert_pdf_date_string(created_date).strftime("%Y-%m-%d %H:%M:%S") if created_date else None
            modified_date_str = convert_pdf_date_string(modified_date).strftime("%Y-%m-%d %H:%M:%S") if modified_date else None

            print(f"Created Date: {created_date_str}")
            print(f"Modified Date: {modified_date_str}")

    except Exception as e:
        print(f"Error: {e}")

app = Flask(__name__)

@app.route('/authenticate', methods=['POST'])
def authenticate():
    auth_data = request.json
    username = auth_data.get('username')
    password = auth_data.get('password')
    if username == 'chirag' and password == 'chirag':
        return jsonify({"message": "Authentication successful"}), 200
    else:
        return jsonify({"message": "Authentication failed"}), 401

if __name__ == '__main__':
    app.run(debug=True)