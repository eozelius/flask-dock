from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def root():
  return jsonify('This text is being served by Flask.')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
