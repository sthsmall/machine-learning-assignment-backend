from flask import Blueprint, request

from servicer import MonitorServicer

monitor_blueprint = Blueprint("monitor", __name__)


@monitor_blueprint.route('/monitor/add', methods=['POST'])
def add_monitor():
    monitor_url = request.args.get('monitor_url')
    monitor_id = request.args.get('monitor_id')

    monitorServicer = MonitorServicer()
    result = monitorServicer.set_monitor(id=monitor_id, url=monitor_url)

    return {"data": result}


@monitor_blueprint.route('/monitor/getAllResult', methods=['P'])
def get_all_result():
    monitorServicer = MonitorServicer()