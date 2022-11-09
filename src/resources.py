from flask import Blueprint, request, jsonify
from database import ResourceGroups, ResourceTypes, GroupResourceTypes, db

resources = Blueprint("resources", __name__, url_prefix="/api/v1/resources")

# / route - GET - will return a paginated list of all resources
@resources.get('/')
def get_all_resources():
    resource_groups_query = ResourceGroups.query.filter(ResourceGroups.approved == True).all()

    if not resource_groups_query:
        return jsonify({'Message': "No resource groups were found"}), 404
    else:
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
                'resource_name': resource_group.resource_name,
                'resource_description': resource_group.resource_description,
                'main_resources': main_resources,
                'location': location,
                'created_at': resource_group.created_at,
                'updated_at': resource_group.updated_at
            })

        return jsonify({'resource_groups': resource_groups}), 200

# /{id} route - GET - will return details of a specific resource by id
@resources.get('/<int:id>')
def get_single_resource(id):
    resource_group = ResourceGroups.query.filter(ResourceGroups.id == id and ResourceGroups.approved == True).first()

    if not resource_group:
        return jsonify({'Message': "Resource group was not found"}), 404
    else:
        return jsonify({
            'id': resource_group.id,
            'resource_name': resource_group.resource_name,
            'resource_description': resource_group.resource_description,
            'business_address_1': resource_group.business_address_1,
            'business_address_2': resource_group.business_address_2,
            'business_city': resource_group.business_city,
            'business_state': resource_group.business_state,
            'business_zip_code': resource_group.business_zip_code,
            'physical_address_1': resource_group.physical_address_1,
            'physical_address_2': resource_group.physical_address_2,
            'physical_city': resource_group.physical_city,
            'physical_state': resource_group.physical_state,
            'physical_zip_code': resource_group.physical_zip_code,
            'website': resource_group.website,
            'phone_number': resource_group.phone_number,
            'email': resource_group.email,
            'instagram': resource_group.instagram,
            'twitter': resource_group.twitter,
            'facebook': resource_group.facebook,
            'venmo': resource_group.venmo,
            'paypal': resource_group.paypal,
            'cash_app': resource_group.cash_app,
            'zelle': resource_group.zelle,
            'additional_contacts': resource_group.additional_contacts,
            'how_to_receive_resources': resource_group.how_to_receive_resources,
            'how_to_donate_resources': resource_group.how_to_donate_resources,
            'notes_for_receiver': resource_group.notes_for_receiver,
            'notes_for_donator': resource_group.notes_for_donator,
            'created_at': resource_group.created_at,
            'updated_at': resource_group.updated_at
        }), 200 

# /{id}/additional route - GET - gets the list of resources available for this specific resource group
@resources.get('/<int:id>/additional')
def get_resource_types_by_resource_group(id):
    resource_group_types = ResourceTypes.query.join(GroupResourceTypes).filter(GroupResourceTypes.resource_group_id == id).all()
    
    if not resource_group_types:
        return jsonify({'Message': "Resource types were not found"}), 404
    else:
        resource_types = []
        for resource_type in resource_group_types:
            resource_types.append({
                'id': resource_type.id,
                'resource_type_name': resource_type.resource_type_name,
            })


        return jsonify({'resource_types': resource_types}), 200
# /search?{searchparams}{serachtype} - GET - returns a list of resources based on the type of search - name, resource type, address

# / POST - creates a new resource submissiion, returns a status back to user to decide what to display to front end
@resources.post('/')
def create_resource():
    body = request.get_json()

    check_resource_name = ResourceGroups.query.filter(ResourceGroups.resource_name == body['resource_name']).first()

    if check_resource_name != None:
        return jsonify({'Message': "Resource group name already exists"}), 409
    else:
        db.session.add(ResourceGroups(
            body['resource_name'], body['resource_description'], body['business_address_1'], body['business_address_2'], body['business_city'], body['business_state'], 
            body['business_zip_code'], body['physical_address_1'], body['physical_address_2'], body['physical_city'], body['physical_state'], body['physical_zip_code'], 
            body['website'], body['phone_number'], body['email'], body['instagram'], body['twitter'], body['facebook'], body['venmo'], body['paypal'], body['cash_app'], 
            body['zelle'], body['additional_contacts']
        ))

        db.session.commit()
        
        return jsonify({
            'Message': "Resource created"
        }), 201
# endpoint for admin review of all unapproved resources
# endpoint for submitting new resource types
# endpoint for viewing all resource types
# endpoint to mark an unapproved resource as approved. This will flip the switch from unapproved to approved and will create the link between resources types and resource groups