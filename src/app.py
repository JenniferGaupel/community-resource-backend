from flask import Flask
from flasgger import Swagger, swag_from
from database import db
from resource_groups import resource_groups
from resource_types import resource_types
import os

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db.app = app
db.init_app(app) 

app.register_blueprint(resource_groups)
app.register_blueprint(resource_types)
