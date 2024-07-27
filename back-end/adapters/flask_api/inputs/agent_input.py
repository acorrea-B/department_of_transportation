from collections.abc import Sequence
from typing import Mapping
from wtforms import StringField, validators, PasswordField
from adapters.flask_api.inputs.base_form import BaseForm
from adapters.flask_api.inputs.password_input import password_validator


class AgentForm(BaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = StringField(
            self.localization.get_message("agent_field_name"),
            [validators.DataRequired(), validators.Length(min=4, max=30)],
        )
        self.identifier = StringField(
            self.localization.get_message("agent_field_identifier"),
            [validators.DataRequired()],
        )
        self.username = StringField(
            self.localization.get_message("agent_field_username"),
            [validators.DataRequired()],
        )
        self.password = PasswordField(
            self.localization.get_message("agent_field_password"), 
            [
                validators.DataRequired(), 
                validators.Length(min=6, message=self.localization.get_message("password_min_length")),
                validators.EqualTo("password_confirm", message=self.localization.get_message('password_not_match')),
                validators.Regexp(
                    r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=])[A-Za-z\d@#$%^&+=]',
                    message=self.localization.get_message('password_structure')
                )
            ]
        )
        self.password_confirm = PasswordField(
            self.localization.get_message("agent_field_repeat_password"),
            [validators.DataRequired()]
        )
    