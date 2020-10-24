from flask import request, jsonify, send_file
from app import app
from app.source.processor import Processor
from app.base.helper import header_option
from json import dumps
from pprint import pprint

PREFIX = '/api/source'


@app.route(PREFIX, methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        print(request.method)
        return jsonify({}), header_option()
    data = request.json
    print(f'{dumps(data)}')
    if not data:
        return jsonify({}), header_option()
    file = Processor().create_file(data)
    pprint(file)
    return jsonify(file) , header_option()
    # return send_file(file,
    #                  mimetype='exe',
    #                  attachment_filename='example.exe',
    #                  as_attachment=True)\
    #     , header_option()