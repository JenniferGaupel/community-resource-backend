from flask import Blueprint, request, jsonify

resources = Blueprint("resources", __name__, url_prefix="/api/v1/bookmarks")

# / route - GET - will return a paginated list of all resources

# /{id} route - GET - will return details of a specific resource by id

# /search?{searchparams}{serachtype} - GET - returns a list of resources based on the type of search - name, resrouce type, address

# /submit POST - creates a new resource submissiion, returns a status back to user to decide what to display to front end
