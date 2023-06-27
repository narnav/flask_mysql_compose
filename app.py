from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@mysql:3306/mydatabase'
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return 'Hello, Flask with MySQL on Docker!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
