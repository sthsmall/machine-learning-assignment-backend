class DetectServicer:
    def __init__(self):
        pass

    def get_detect_result(self, id):
        return {"data": "this is a detect test" + str(id)}
