from enum import unique
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import string
import random

db = SQLAlchemy()


class ResourceGroups(db.Model):
    __tablename__ = "resource_groups"
    id = db.Column(db.Integer, primary_key=True)
    resource_name = db.Column(db.String(), unique=True, nullable=False)
    resource_description = db.Column(db.String())
    business_address_1 = db.Column(db.String())
    business_address_2 = db.Column(db.String())
    business_city = db.Column(db.String())
    business_state = db.Column(db.String())
    business_zip_code = db.Column(db.String())
    physical_address_1 = db.Column(db.String())
    physical_address_2 = db.Column(db.String())
    physical_city = db.Column(db.String())
    physical_state = db.Column(db.String())
    physical_zip_code = db.Column(db.String())    
    website = db.Column(db.String())
    phone_number = db.Column(db.String())
    email = db.Column(db.String())
    instagram = db.Column(db.String())
    twitter = db.Column(db.String())
    facebook = db.Column(db.String())
    vanmo = db.Column(db.String())
    paypal = db.Column(db.String())
    cash_app = db.Column(db.String())
    zelle = db.Column(db.String())    
    additional_contacts = db.Column(db.String())
    how_to_receive_resources = db.Column(db.String())   
    how_to_donate_resources = db.Column(db.String())   
    notes_for_receiver = db.Column(db.String())   
    notes_for_donator = db.Column(db.String())   
    approved = db.Column(db.Boolean, default=False, nullable=False)    
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    resource_group_types = db.relationship('GroupResourceTypes', backref="resource_groups")

    def __repr__(self) -> str:
        return 'ResourceGroups: {self.resource_name}'


class ResourceTypes(db.Model):
    __tablename__ = "resource_types"
    id = db.Column(db.Integer, primary_key=True)
    resource_type_name = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    resource_group_types = db.relationship('GroupResourceTypes', backref="resource_types")

    def __repr__(self) -> str:
        return 'ResourceType: {self.resource_type_name}'

class GroupResourceTypes(db.Model):
    __tablename__ = "group_resource_types"
    id = db.Column(db.Integer, primary_key=True)
    resource_group_id = db.Column(db.Integer, db.ForeignKey('resource_groups.id'), nullable=False)
    resource_type_id = db.Column(db.Integer, db.ForeignKey('resource_types.id'), nullable=False)   
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __repr__(self) -> str:
        return 'GroupResourceTypes: {self.id}'        
