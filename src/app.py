from flask import Flask, request, jsonify
from database import db, ResourceGroups
from resources import resources
import os
from seed_data import triiibe_foundation, resource_type_list, group_resource_type_list
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db.app = app
db.init_app(app) 

app.register_blueprint(resources)

# db.session.add_all(group_resource_type_list)
# db.session.commit()
# db.session.add_all(resource_type_list)
# db.session.commit()
# db.session.add(triiibe_foundation)
# db.session.commit()

# db.session.add(triiibe_foundation)
# db.session.commit()
# db.create_all()
# db.drop_all()