from flask.ext.wtf import Form
from wtforms import SubmitField,StringField
from wtforms.validators import Required


class NameForm(Form):
    name = StringField('what is your name?',validators=[Required()])
    submit = SubmitField('Submit')

