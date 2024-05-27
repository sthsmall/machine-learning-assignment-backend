class Monitor:
    def __init__(self, id=None, url=None):
        self.id = id
        self.url = url
    def __str__(self):
        return "id: " + str(self.id) + " url: " + self.url