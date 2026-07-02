# explore the 'Flask module and create a web server using flask & python


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>Hellow, world!</P>"

app.run()