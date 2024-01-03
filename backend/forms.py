from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, URLField
from wtforms.validators import Optional, InputRequired, URL



class RegisterUser(FlaskForm):
    '''form for registering a new user'''

    username = StringField(
        'username',
        validators=[InputRequired()]
    )

    first_name = StringField(
        'first name',
        validators=[InputRequired()]
    )

    last_name = StringField(
        'last name',
        validators=[InputRequired()]
    )







