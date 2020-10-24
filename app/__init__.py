from flask import Flask


app = Flask(__name__
            , static_folder='dist'
            )
app.config['JSON_AS_ASCII'] = False
