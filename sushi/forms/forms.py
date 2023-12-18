from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FileField,PasswordField
from wtforms.validators import DataRequired, Length, Email, NumberRange, regexp, InputRequired

class CreateProductForm(FlaskForm):
    """The new product form"""
    name        = StringField("Name", validators=[DataRequired(), Length(min=1, max=30)])
    description = StringField("Description (components)", validators=[DataRequired(), Length(min=20, max=360)])
    mass        = IntegerField("Mass (volume)", validators=[DataRequired()])
    price       = IntegerField("Price (uah)", validators=[DataRequired()])
    image       = FileField('Image File', [regexp(r'^[^/\\]\.jpg$')])
    submit      = SubmitField("Save")

class LogInForm(FlaskForm):
    email       = StringField("Email", [DataRequired(), Email(), Length(min=5, max=30)], render_kw={"placeholder": "name@gmail.com"})
    password    = PasswordField("Password", [DataRequired()],render_kw={"placeholder": "******"})
    submit      = SubmitField("Log in")

