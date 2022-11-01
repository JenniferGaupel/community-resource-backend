from enum import unique
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import string
import random

db = SQLAlchemy()


class ResourceGroups(db.Model):
    __tablename__ = "resource_groups"
    id = db.Column(db.Integer, primary_key=True)
    resource_name = db.Column(db.String(80), unique=True, nullable=False)
    resource_description = db.Column(db.String(120))
    business_address = db.Column(db.String(120))
    physical_address = db.Column(db.String(120))
    website = db.Column(db.String(120))
    phone_number = db.Column(db.String(120))
    email = db.Column(db.String(120))
    instagram = db.Column(db.String(120))
    twitter = db.Column(db.String(120))
    facebook = db.Column(db.String(120))
    vanmo = db.Column(db.String(120))
    paypal = db.Column(db.String(120))
    cash_app = db.Column(db.String(120))
    zelle = db.Column(db.String(120))    
    additional_contacts = db.Column(db.String(120))
    how_to_receive_resources = db.Column(db.String(120))   
    how_to_donate_resources = db.Column(db.String(120))   
    notes_for_receiver = db.Column(db.String(120))   
    notes_for_donator = db.Column(db.String(120))   
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    resource_group_types = db.relationship('GroupResourceTypes', backref="resource_groups")

    def __repr__(self) -> str:
        return 'ResourceGroups: {self.resource_name}'


class ResourceTypes(db.Model):
    __tablename__ = "resource_types"
    id = db.Column(db.Integer, primary_key=True)
    resource_type_name = db.Column(db.String(80), unique=True, nullable=False)
    resource_type_description = db.Column(db.String(120))
    main_resource_type = db.Column(db.Boolean, default=True, nullable=False)
    detailed_resource_type = db.Column(db.Boolean, default=True, nullable=False)
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
    available = db.Column(db.Boolean, default=True)
    needed = db.Column(db.Boolean, default=False)    
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __repr__(self) -> str:
        return 'GroupResourceTypes: {self.id}'        



class SubmittedResources(db.Model):
    __tablename__ = "submitted_resources"
    id = db.Column(db.Integer, primary_key=True)
    resource_name = db.Column(db.String(80), unique=True, nullable=False)
    resource_description = db.Column(db.String(120))
    business_address = db.Column(db.String(120))
    physical_address = db.Column(db.String(120))
    website = db.Column(db.String(120))
    phone_number = db.Column(db.String(120))
    email = db.Column(db.String(120))
    instagram = db.Column(db.String(120))
    twitter = db.Column(db.String(120))
    facebook = db.Column(db.String(120))
    vanmo = db.Column(db.String(120))
    paypal = db.Column(db.String(120))
    cash_app = db.Column(db.String(120))
    zelle = db.Column(db.String(120))
    additional_contacts = db.Column(db.String(120))
    entered_to_resource_group = db.Column(db.Boolean, default=False)    
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __repr__(self) -> str:
        return 'SubmittedResource: {self.resource_name}'
