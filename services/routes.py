from flask import Blueprint, render_template

services_blueprint = Blueprint('Services', __name__)

@services_blueprint.route('/Sea-Freight')
def sea_freight():
    return render_template ("Services/sea.html")

@services_blueprint.route('/Air-Freight')
def air_freight():
    return render_template ("Services/air.html")

@services_blueprint.route('/Warehousing-&-Fulfillment')
def FC():
    return render_template ("Services/fulfillment.html")

@services_blueprint.route('/Road-Freight')
def road_freight():
    return render_template ("Services/road.html")

@services_blueprint.route('/Project-Cargo')
def project_cargo():
    return render_template ("Services/project.html")