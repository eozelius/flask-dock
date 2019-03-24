from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'hot pie what is going on? 7:37 asdf'

if __name__ == '__main__':
  app.run(
    debug=True,
    host='0.0.0.0',
    port=80
  )
