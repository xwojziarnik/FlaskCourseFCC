from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        """
        FlaskForm class is pure magic! While executing the form Flask is going to search for every method
        that has a 'validate_' in its name. If there is any, Flask will execute that method at first.

        Moreover, Flask will search for field that is in method name (in this case it's '..username') and
        that Flask is connecting field with a method.

        So, in our case Flask is checking for any user with username which is already in use.

        Remember to add '.data' at the end of query - it must be the same as we implemented in routes.py:
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        """
        user = User.query.filter_by(username=username_to_check.data).first()

        if user:
            raise ValidationError("Username already exist. Please try to use a different username.")

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()

        if email_address:
            raise ValidationError("Email address in use. Please try another one.")

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='E-mail Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=4), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')
