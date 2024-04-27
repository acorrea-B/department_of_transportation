class Agent:
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

    def to_dict(self):
        return {"name": self.name, "identifier": self.identifier}
