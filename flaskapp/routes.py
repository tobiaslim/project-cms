# Each resource class will register their end point in this file
# Define methods in the file in the resource folder
from flaskapp import api, db
from .resource.OperatorResource import OperatorResource
from .resource.GovernmentOfficialResource import GovernmentOfficialResource
from .resource.IncidentResource import IncidentResource
from .resource.ListIncidentResource import ListIncidentResource
from .resource.GPIncidentResource import GPIncidentResource
from .resource.SessionResource import SessionResource
from .resource.GPmobileResource import GPmobileResource
from .resource.SocialMediaResource import SocialMediaResource
from .resource.IncidentUpdateResource import IncidentUpdateResource
from .model.User import User
from .resource.WeatherResource import WeatherResource
from .resource.PSIResource import PSIResource
from .resource.DengueResource import DengueResource

api.add_resource(OperatorResource, '/user/operator')
api.add_resource(GovernmentOfficialResource, '/user/governmentofficial')
api.add_resource(IncidentResource, '/incident', '/incident/<int:incident_id>')
api.add_resource(ListIncidentResource, '/allIncidents')
api.add_resource(GPIncidentResource, '/gpincident')
api.add_resource(SessionResource, '/session')
api.add_resource(GPmobileResource, '/gpmobile')
api.add_resource(SocialMediaResource, '/socialmedia')
api.add_resource(WeatherResource, '/weather')
api.add_resource(PSIResource, '/psi')
api.add_resource(DengueResource, '/dengue')
api.add_resource(IncidentUpdateResource, '/incidentupdate/<string:urlpath>')
