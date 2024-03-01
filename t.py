import os
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/authenticate', methods=['POST'])
def authenticate_and_show_file_times():
    auth_data = request.json
    username = auth_data.get('username')
    password = auth_data.get('password')
    if username == 'chirag' and password == 'chirag':
        return jsonify(show_file_times()), 200
    else:
        return jsonify({"message": "Authentication failed"}), 401

def show_file_times():
    path = r"C:\Users\chira\Desktop\iimjobs_Sneha_Raosaheb_Patil (1).pdf"
    ti_c = os.path.getctime(path)
    ti_m = os.path.getmtime(path)
    c_ti = time.ctime(ti_c)
    m_ti = time.ctime(ti_m)
    return {
        "created_time": c_ti,
        "modified_time": m_ti,
        "path": path
    }

if __name__ == '__main__':
    app.run(debug=True)