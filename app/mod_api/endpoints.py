from flask import Blueprint
from flask_restful import Resource, Api, reqparse
from sqlalchemy.exc import IntegrityError
from app import db
from app.models import Email



api_blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_blueprint)

parser = reqparse.RequestParser()
parser.add_argument('email', type=str, help="Email is required", location=['json'])
parser.add_argument('source', type=str, help="Source", location=['json'])
parser.add_argument('form_data_as_json', type=str, location=['json'])


class SignUp(Resource):
	def post(self):
		args = parser.parse_args()
		if Email.query.filter(Email.email==args.get('email'), Email.source==args.get('source')).first():
			return {'message':"Thanks for signing up"}
		else:
			email = Email(email=args.get('email'), source=args.get('source'), form_data_as_json=args.get('form_data_as_json'))
			try:
				db.session.add(email)
				db.session.commit()
			except IntegrityError:
				return {'message':"Error signing up"}  , 500
		return {'message':"Thanks for signing up"}

api.add_resource(SignUp,'/sign-up')
