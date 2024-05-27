from flask import Blueprint

test_blueprint = Blueprint("test", __name__)


@test_blueprint.route('/test', methods=['GET'])
def test():
    return {"data": "this is a test"}
