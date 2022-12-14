from flask import Blueprint, request, jsonify, current_app
from flasgger import swag_from
from database import ResourceGroups, ResourceTypes, GroupResourceTypes, db, ResourceGroupsSchema
import json

resource_groups = Blueprint("resource_groups", __name__, url_prefix="/api/v1/resource-groups")

@resource_groups.get('/')
@swag_from('./docs/resource_groups/get_all_approved.yaml')
def get_all_approved_resources():
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
                'location': location
            })

        return jsonify({'resource_groups': resource_groups}), 200

@resource_groups.get('/<int:id>')
@swag_from('./docs/resource_groups/get_single.yaml')
def get_single_resource(id):
    resource_group = ResourceGroups.query.filter(ResourceGroups.id == id).first()

    if not resource_group:
        return jsonify({'Message': "Resource group was not found"}), 404
    else:
        resource_types_query = ResourceTypes.query.join(GroupResourceTypes).filter(GroupResourceTypes.resource_group_id == resource_group.id).all()
        
        resource_types = ""
        for resource_type in resource_types_query:            
            resource_types += resource_type.resource_type_name + ", "        
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
            'resource_types': resource_types,
            'created_at': resource_group.created_at,
            'updated_at': resource_group.updated_at
        }), 200 

@resource_groups.get('/<int:id>/resource-types')
@swag_from('./docs/resource_groups/get_single.yaml')
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

# @resource_groups.get('/search/<string:search_value>/<string:search_type>')
# def resource_group_search(search_value, search_type):
#     # trim & check the search value
    
#     if search_type == "name":
#         # resource type
#     elif search_type == "resource-type":
#         # resource type
#     elif search_type == "address":
#         # resource address for all areas
#     else:
#         # return error

@resource_groups.post('/submit-resource')
@swag_from('./docs/resource_groups/create.yaml')
def create_resource_group():
    new_resource_name = request.get_json()['resource_name']
    
    if new_resource_name == None or new_resource_name == "":
        return jsonify({'Message': "Resource name is required"}), 400
    else:
        check_resource_name = ResourceGroups.query.filter_by(resource_name = new_resource_name).first()
        
        if check_resource_name:
            return jsonify({'Message': "Resource group with name " + check_resource_name.resource_name + " already exists"}), 409
        else:
            rg_schema = ResourceGroupsSchema()
            new_rg = rg_schema.load(request.get_json(), session=db.session)
            
            db.session.add(new_rg)
            db.session.commit()
            
            return rg_schema.dump(new_rg), 201            

@resource_groups.delete('/<int:id>')
@swag_from('./docs/resource_groups/delete.yaml')
def delete_resource_group(id):
    group_resource_type_query = GroupResourceTypes.query.filter(GroupResourceTypes.resource_group_id == id).all()

    if group_resource_type_query != None:
        for group_resource_type in group_resource_type_query:
            db.session.delete(group_resource_type)
            db.session.commit()

    resource_group = ResourceGroups.query.filter(ResourceGroups.id == id).first()

    if resource_group != None:
        db.session.delete(resource_group)
        db.session.commit()

        return jsonify({}), 204

    else:
        return jsonify({'message': "Resource group not found"}), 404

@resource_groups.get('/unapproved')
@swag_from('./docs/resource_groups/get_all_unapproved.yaml')
def get_unapproved_resources():
    resource_groups_query = ResourceGroups.query.filter(ResourceGroups.approved == False).all()

    if not resource_groups_query:
        return jsonify({'Message': "No resource groups were found"}), 404
    else:
        resource_groups = []

        for resource_group in resource_groups_query:
            
            resource_groups.append({
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
                'approved': resource_group.approved,
                'created_at': resource_group.created_at,
                'updated_at': resource_group.updated_at,
                'unapproved_resource_list': resource_group.unapproved_resource_list
            })

        return jsonify({'resource_groups': resource_groups}), 200

@resource_groups.put('/<int:id>/approve')
@resource_groups.patch('/<int:id>/approve')
def approve_resource_group(id):
    resource_group = ResourceGroups.query.filter(ResourceGroups.id == id).first()

    if resource_group == None:
        return jsonify({'Message': "Resource group not found"}), 404
    elif resource_group.approved == True:
        return jsonify({'Message': "Resource group is already approved"}), 409
    else:
        # body = request.get_json()

        # for resource_type in body['resource_types']:
        #     resource_type_query = ResourceTypes.query.filter(ResourceTypes.id == resource_type.id).first()
        #     if resource_type_query == None:
        #         return jsonify({'Message': "Resource type " +  resource_type.resource_type_name + " not found"}), 404
        #     else:
        #         group_resource_Type = GroupResourceTypes(
        #             resource_group_id = id, resource_type_id = resource_type.id
        #         )

        #         db.session.add(group_resource_Type)
        #         db.session.commit()
                
        resource_group.approved = True
        db.session.commit()
        
        return jsonify({'Message': "Resource group " + resource_group.resource_name + " has been approved"}), 200
