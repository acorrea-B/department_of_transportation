class Vehicle:
    def __init__(self, license_plate, brand, color, owner):
        self.license_plate = license_plate
        self.brand = brand
        self.color = color
        self.owner = owner

    def to_dict(self):
        return {
            "license_plate": self.license_plate,
            "brand": self.brand,
            "color": self.color,
            "owner": self.owner,
        }
