from . import app
from . import jsonify
from . import api
from . import resources


api.add_resource(resources.SignInResource, '/api/v1/sign-in')
api.add_resource(resources.SignUpResource, '/api/v1/sign-up')
api.add_resource(resources.LogOutResource, '/api/v1/logout')
api.add_resource(resources.LogOutRefreshResource, '/api/v1/logout/refresh')
api.add_resource(resources.SignInRefreshResource, '/api/v1/sign-in/refresh')
api.add_resource(resources.VerifyResource, '/api/v1/verify')


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index():
	"""
	The main info route.
	Return the basic info
	"""
	response = {
		'message': 'The customer product CRM REST API',
		'version': '1.0.0'
	}

	return jsonify(response) 

