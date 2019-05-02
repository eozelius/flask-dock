from flask import Flask
from flask import jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
frontend_ip = os.environ['FRONTEND_IP']
CORS(app, resources={r"*": {"origins": frontend_ip}})

@app.route('/')
def root():
  return jsonify(frontend_ip)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
