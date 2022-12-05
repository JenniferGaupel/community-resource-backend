from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from database import db
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from resource_groups import resource_groups
from resource_types import resource_types
import os
from config.swagger import template, swagger_config

app = Flask(__name__)
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') 

db = SQLAlchemy(app)
ma = Marshmallow(app)
db.app = app
db.init_app(app) 

app.register_blueprint(resource_groups)
app.register_blueprint(resource_types)

Swagger(app, config=swagger_config, template=template)
