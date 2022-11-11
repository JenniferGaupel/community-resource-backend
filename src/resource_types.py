from flask import Blueprint, request, jsonify
from database import ResourceTypes, GroupResourceTypes, db

resource_types = Blueprint("resource_types", __name__, url_prefix="/api/v1/resource-types")

# endpoint for viewing all resource types
@resource_types.get('/')
def get_all_resource_types():
    resource_types_query = ResourceTypes.query.all()

    if resource_types_query == None:
        return jsonify({'Message': "No resource types were found"}), 404
    else:
        resource_types = []

        for resource_type in resource_types_query:
            resource_types.append({
                'id': resource_type.id,
                'resource_type_name': resource_type.resource_type_name,
                'created_at': resource_type.created_at,
                'updated_at': resource_type.updated_at,
            })

        return jsonify({'resource_types': resource_types}), 200    

# view single resource type
@resource_types.get('/<int:id>')
def get_resource_type():
    resource_type = ResourceTypes.query.filter(ResourceTypes.id == id).first()

    if resource_type == None:
        return jsonify({'Message': "Resource type not found"}), 404
    else:
        return jsonify({
            'id': resource_type.id,
            'resource_type_name': resource_type.resource_type_name,
            'created_at': resource_type.created_at,
            'updated_at': resource_type.updated_at,
        }), 200

# new resource type
@resource_types.post('/')
def create_resource_type():
    body = request.get_json()

    if body['resource_type_name'] == None:
        return jsonify({'Message': "Resource type name is required"}), 400
    else:
        check_resource_type_name = ResourceTypes.query.filter(ResourceTypes.resource_type_name == body['resource_type_name']).first()

        if check_resource_type_name != None:
            return jsonify({'Message': "Resource type name already exists"}), 409
        else:
            new_resource_type = ResourceTypes(
                resource_type_name = body['resource_type_name']
            ) 
            db.session.add(new_resource_type)

            db.session.commit()
            
            return jsonify({
                'Message': "Resource group "  + new_resource_type.resource_type_name + " created"
            }), 201    


# edit resource type
# @resource_types.put('/<int:id>')
# @resource_types.patch('/<int:id>')
# def edit_resource_type(id):
#     resource_type = ResourceTypes.query.filter(ResourceTypes.id == id).first()

#     if resource_type == None:
#         return jsonify({'Message': "Resource type not found"}), 404
#     else:


# delete resource type
@resource_types.delete('/<int:id>')
def delete_resource_type(id):
    group_resource_type_query = GroupResourceTypes.query.filter(GroupResourceTypes.resource_type_id == id).all()

    if group_resource_type_query != None:
        for group_resource_type in group_resource_type_query:
            db.session.delete(group_resource_type)
            db.session.commit()

    resource_type = ResourceTypes.query.filter(ResourceTypes.id == id).first()

    if resource_type != None:
        db.session.delete(resource_type)
        db.session.commit()

        return jsonify({}), 204

    else:
        return jsonify({'message': "Resource type not found"}), 404
