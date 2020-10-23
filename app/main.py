from app import app
from app.source import view


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=13452)
