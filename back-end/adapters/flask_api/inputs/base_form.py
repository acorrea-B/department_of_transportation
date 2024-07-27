from wtforms import Form


class BaseForm(Form):
    def __init__(
        self,
        formdata=None,
        obj=None,
        prefix="",
        data=None,
        meta=None,
        localization=None,
        **kwargs,
    ):
        super().__init__(formdata, obj, prefix, data, meta, **kwargs)
        self.localization = localization
