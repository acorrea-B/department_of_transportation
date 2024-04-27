class Violation:
    def __init__(self, license_plate, timestamp, comments):
        self.license_plate = license_plate
        self.timestamp = timestamp
        self.comments = comments

    def to_dict(self):
        return {
            "license_plate": self.license_plate,
            "timestamp": self.timestamp,
            "comments": self.comments,
        }
