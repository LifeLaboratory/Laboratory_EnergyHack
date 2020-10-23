from flask import request, jsonify
from app import app
from app.source.processor import Processor
from app.base.helper import header_option

PREFIX = '/api/source'


@app.route(PREFIX, methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        print(request.method)
        return jsonify({}), header_option()
    data = request.json
    print(f'data = {data}')
    return jsonify(Processor().create_file()), header_option()
