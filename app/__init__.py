from flask import Flask
from Productos.Models import prod
app = Flask(__name__)


app.register_blueprint(prod)
if __name__ == "__main__":
    app.run(debug=True)



