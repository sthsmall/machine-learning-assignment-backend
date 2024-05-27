from utils.singleton import singleton

@singleton
class MonitorManager:
    def __init__(self):
        self.monitors = {}

    def add_monitor(self, monitor):
        self.monitors[monitor.id] = monitor

    def get_monitor(self, name):
        return self.monitors.get(name)