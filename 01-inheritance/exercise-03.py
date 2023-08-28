import json

class Output:
    def __init__(self):
        pass

    def to_json(self):
        return json.dumps(self)


class SimpleRow(dict, Output):
    def __init__(self):
        super().__init__()


class SimpleTable(list, Output):
    def __init__(self):
        super().__init__()


