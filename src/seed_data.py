from database import ResourceGroups, ResourceTypes, GroupResourceTypes, db

#triiibefoundation
#cincinnatiforjustice
#thefridgecincy
#cincyccs
#covunityfridge
#jens test with all fields filled out

triiibe_foundation = ResourceGroups(resource_name="Triiibe Foundation", resource_description="Provide positive representation of urban culture through growth, community, and creativity.",
    business_address_1="PO Box 14723", business_city="Cincinnati", business_state="OH", business_zip_code="45250", website="https://www.triiibefoundation.org/", email="info@triiibefoundation.org",
    instagram="triiibefoundation", facebook="TriiibeFoundation", paypal="https://www.paypal.com/us/fundraiser/charity/3925960", 
    additional_contacts="linktr.ee/triiibefoundation, https://www.linkedin.com/company/triiibefoundation/, https://www.youtube.com/channel/UCWUcgH1h3rT4yIjAyYhJc2w",
    how_to_receive_resources="Multiple programs. Potluck 4 the People is the last Sunday of each month, typically at Piatt Park. See website for more deatisl. Provides lunch, clothing, haircyuts, medical services and more. Garden Parcels Triiibe Works:Workforce development program . See website for details and how to sign up. Garden Parcels Youth Space: A youth program to help stufents heal in place of alientation or punishment. See the website to reach out about a student who could benefit.",
    how_to_donate_resources="Donate money via the Paypal link. See the website to sign up to receive emails about upcoming involvement opportunities. Bring clothing, resources food, skills to the potluck for the people. Check their social media for needed resources, or sign up to be a Potluck 4 the People volunteer on the website.",
    approved=True
)
##################################################################################
resource_type_list = []

resource_type_clothes = ResourceTypes(
    resource_type_name="Clothes"
)
resource_type_list.append(resource_type_clothes)

resource_type_food = ResourceTypes(
    resource_type_name="Food"
)
resource_type_list.append(resource_type_food)

resource_type_hair_cut = ResourceTypes(
    resource_type_name="Hair cut and/or Shave"
)
resource_type_list.append(resource_type_hair_cut)

resource_type_medical_aid = ResourceTypes(
    resource_type_name="Medical Aid"
)
resource_type_list.append(resource_type_medical_aid)

resource_type_narcan = ResourceTypes(
    resource_type_name="Narcan"
)
resource_type_list.append(resource_type_narcan)

resource_type_medical_training = ResourceTypes(
    resource_type_name="Medical Training"
)
resource_type_list.append(resource_type_medical_training)

resource_type_narcan_training = ResourceTypes(
    resource_type_name="Narcan Training"
)
resource_type_list.append(resource_type_narcan_training)

resource_type_water_on_site = ResourceTypes(
    resource_type_name="Water on site"
)
resource_type_list.append(resource_type_water_on_site)
##################################################################################

group_resource_type_list = []

group_resource_type1=GroupResourceTypes(
    resource_group_id=1, resource_type_id=1
)
group_resource_type_list.append(group_resource_type1)

group_resource_type2=GroupResourceTypes(
    resource_group_id=1, resource_type_id=2
)
group_resource_type_list.append(group_resource_type2)

group_resource_type3=GroupResourceTypes(
    resource_group_id=1, resource_type_id=3
)
group_resource_type_list.append(group_resource_type3)

group_resource_type4=GroupResourceTypes(
    resource_group_id=1, resource_type_id=4
)
group_resource_type_list.append(group_resource_type4)
