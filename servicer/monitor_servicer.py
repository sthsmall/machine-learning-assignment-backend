from DTO import Monitor
from utils.monitor_manger import MonitorManager


class MonitorServicer():
    def __init__(self):
        pass

    def set_monitor(self, id ,url) -> str:
        monitor = Monitor(id, url)
        monitorManger = MonitorManager()
        monitorManger.add_monitor(monitor)
        return "add monitor success"
