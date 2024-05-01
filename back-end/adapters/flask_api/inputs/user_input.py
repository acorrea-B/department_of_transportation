from wtforms import Form, StringField, EmailField, validators


class RegisterUserForm(Form):
    name = StringField(
        "name", [validators.DataRequired(), validators.Length(min=4, max=30)]
    )
    email = EmailField("Email Address", [validators.DataRequired(), validators.Email()])
