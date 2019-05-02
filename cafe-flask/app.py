from flask import Flask
from flask import jsonify
from flask_cors import CORS

'''
  app = Flask(__name__)
  CORS(app)

  @app.route("/")
  def helloWorld():
    return "Hello, cross-origin-world!"

'''

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/')
def root():
  return jsonify('This text is being served by Flask.')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
