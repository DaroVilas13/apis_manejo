import requests
from flask import Flask, request, Response
from caso_01_funcion import get_patiotuerca
import json
import os


app =Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'hola mundo'

@app.route('/api/patiotuerca')
def get_patio_tuerca_precio_promedio():
    query = request.args.get('search_text')
    if query is None:
        return Response(json.dumps({"error": "missing 'search_text' query-parameter"}), status=400, mimetype='application/json')

    return Response(json.dumps(get_patiotuerca(query)), status=200, mimetype='application/json')




if __name__ == '__main__':
    app.run()
    