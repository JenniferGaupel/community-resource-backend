from flask import Flask
from database import db
from resource_groups import resource_groups
from resource_types import resource_types
import os
# from seed_data import resource_type_list, group_resource_type_list
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db.app = app
db.init_app(app) 

app.register_blueprint(resource_groups)
app.register_blueprint(resource_types)

# db.session.add_all(group_resource_type_list)
# db.session.commit()

# db.session.add_all(resource_type_list)
# db.session.commit()

# db.session.add(jen_sample_approved)
# db.session.commit()

# db.create_all()
# db.drop_all()