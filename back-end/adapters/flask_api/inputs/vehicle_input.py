from wtforms import Form, StringField, EmailField, validators


class CreateVehicleForm(Form):
    license_plate = StringField(
        "LicensePlate", [validators.DataRequired(), validators.Length(min=4, max=30)]
    )
    owner_email = EmailField(
        "OwnerEmail", [validators.DataRequired(), validators.Email()]
    )
    color = StringField(
        "Color", [validators.DataRequired(), validators.Length(min=4, max=30)]
    )
    brand = StringField(
        "Brand", [validators.DataRequired(), validators.Length(min=4, max=50)]
    )


class UpdateVehicleForm(Form):
    license_plate = StringField(
        "LicensePlate", [validators.DataRequired(), validators.Length(min=4, max=30)]
    )
    owner_email = EmailField("OwnerEmail", [validators.Email()])
    color = StringField("Color", [validators.Length(min=4, max=30)])
