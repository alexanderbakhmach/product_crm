from . import Resource
from . import parsers
from . import ClusterRpcProxy
from . import app
from . import jsonify


class SignInResource(Resource):
    def post(self):
        data = parsers.sign_in_parser.parse_args()
        return 'test'


class VerifyResource(Resource):
    def post(self):
        data = parsers.verify_parser.parse_args()
        return 'test'


class SignUpResource(Resource):
    def post(self):
        data = parsers.sign_up_parser.parse_args()
        cluster_rpc_proxy_address = app.config.get('NAMEKO_CONFIG')

        with ClusterRpcProxy(cluster_rpc_proxy_address) as rpc:
            email = data.get('email')
            password = data.get('password')

            sign_up_data = rpc.authentication_service.sign_up(email, password)

            print(sign_up_data)
            
        return sign_up_data


class LogOutResource(Resource):
    def post(self):
        return 'test'


class LogOutRefreshResource(Resource):
    def post(self):
        return 'test'


class SignInRefreshResource(Resource):
    def post(self):
        return 'test'
