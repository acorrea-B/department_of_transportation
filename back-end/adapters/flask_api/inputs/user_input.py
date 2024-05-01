from wtforms import Form, StringField, EmailField, validators


class UserForm(Form):
    name = StringField(
        "name", [validators.DataRequired(), validators.Length(min=4, max=30)]
    )
    email = EmailField("Email Address", [validators.DataRequired(), validators.Email()])
