from wtforms import Form, StringField, EmailField, validators


class AgentForm(Form):
    name = StringField(
        "Name", [validators.DataRequired(), validators.Length(min=4, max=30)]
    )
    identifier = StringField("Agent identification", [validators.DataRequired()])
