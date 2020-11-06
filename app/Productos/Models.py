
from flask import Blueprint
from flask import Flask, Response

prod = Blueprint('prod',__name__,url_prefix='/prod')

@prod.route('/<nombre>')
def get_product(nombre):
    if(nombre != "pygroup"):
        return Response("Felicitaciones! Trabajo exitoso{}".format(nombre), status = 200)
    else:
        return Response("ERROR! No se puede usar el nombre pygroup", status = 400)