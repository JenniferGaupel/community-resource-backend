from flask import Blueprint, request, jsonify
from database import ResourceGroups, ResourceTypes, GroupResourceTypes, db

resources = Blueprint("resources", __name__, url_prefix="/api/v1/resources")

# / route - GET - will return a paginated list of all resources
@resources.get("/")
def get_all_resources():
    resource_groups_query = ResourceGroups.query.filter(ResourceGroups.approved == True).all()

    resource_groups = []

    for resource_group in resource_groups_query:
        if(resource_group.physical_city != None and resource_group.physical_state != None):
            location = resource_group.physical_city + ", " + resource_group.physical_state
        elif(resource_group.business_city != None and resource_group.business_state != None):
            location = resource_group.business_city + ", " + resource_group.business_state
        else:
            location = "Area Unknown"

        main_resources_query = ResourceTypes.query.join(GroupResourceTypes).filter(GroupResourceTypes.resource_group_id == resource_group.id).all()
        
        main_resources = ""
        for main_resource in main_resources_query:            
            main_resources += main_resource.resource_type_name + ", "

        resource_groups.append({
            'id': resource_group.id,
            'name': resource_group.resource_name,
            'description': resource_group.resource_description,
            'main_resources': main_resources,
            'location': location,
            'created_at': resource_group.created_at,
            'updated_at': resource_group.updated_at
        })

    return jsonify({'resource_groups': resource_groups}), 200

# /{id} route - GET - will return details of a specific resource by id
@resources.get('/<int:id>')
def get_resource(id):
    resource_groups_query = ResourceGroups.query.filter(ResourceGroups.id == id).first()

    if not resource_groups_query:
        return jsonify({'Message': "Item not found"}), 404
    else:
        

# /search?{searchparams}{serachtype} - GET - returns a list of resources based on the type of search - name, resrouce type, address

# /submit POST - creates a new resource submissiion, returns a status back to user to decide what to display to front end
