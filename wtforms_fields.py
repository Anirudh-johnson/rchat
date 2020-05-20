from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    """ Registration form"""

    username = StringField('username_label',
        validators=[InputRequired(message='username required'),
        Length(min=4, max=25, message="username must be between 4 and 25 characters")])
    password = PasswordField('password_label',
        validators=[InputRequired(message='password required'),
        Length(min=4, max=25, message="password must be between  4 and 25 characters")])
    confirm_pswd = PasswordField('confirm_pswd_label',
        validators=[InputRequired(message='password required'),
        EqualTo('password', message="Password must match")])
    submit_button = SubmitField('Create')
