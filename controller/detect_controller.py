from flask import request, Blueprint
from servicer import DetectServicer

detect_blueprint = Blueprint("detect", __name__)


@detect_blueprint.route('/detect', methods=['GET'])
def get_detect_result():
    monitor_id = request.args.get('monitor_id')

    detectServicer = DetectServicer()

    result = detectServicer.get_detect_result(id=monitor_id)
    return {"data": result}
