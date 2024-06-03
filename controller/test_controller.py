from flask import Blueprint,request
from flask_cors import CORS
test_blueprint = Blueprint("test", __name__)


@test_blueprint.route('/test', methods=['POST','GET'])
def test():
    print(request.get_json())
    # print(request.get_data())
    return[{"id": 1,"status": 1},{"id": 2,"status": 2}]

