from flask_restful import Api, Resource

api = Api()

class Register(Resource):
    def post(self):
        # Handle registration
        return {"message": "Registration successful"}

class ApplyLoan(Resource):
    def post(self):
        # Handle loan application
        return {"message": "Loan application submitted"}

api.add_resource(Register, '/register')
api.add_resource(ApplyLoan, '/apply_loan')
