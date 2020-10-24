from flask import request, jsonify, send_file
from app import app
from app.source.processor import Processor
from app.base.helper import header_option
from json import dumps


PREFIX = '/api/source'


@app.route(PREFIX, methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        print(request.method)
        return jsonify({}), header_option()
    data = request.json
    print(f'{dumps(data)}')
    file = Processor().create_file(data)
    return send_file(file,
                     mimetype='exe',
                     attachment_filename='example.exe',
                     as_attachment=True)\
        , header_option()
