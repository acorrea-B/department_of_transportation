class User:
    def __init__(self, name, email, id=None, updated_at=None):
        self.name = name
        self.email = email
        self.id = id
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "id": self.id,
            "updated_at": self.updated_at,
        }
