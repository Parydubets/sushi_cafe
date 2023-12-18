from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FileField,PasswordField
from wtforms.validators import DataRequired, Length, Email, NumberRange, regexp, InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class CreateProductForm(FlaskForm):
    """The new product form"""
    name        = StringField("Name", validators=[DataRequired(), Length(min=1, max=30)],render_kw={"placeholder": "Product name"})
    description = StringField("Description (components)", validators=[DataRequired(), Length(min=20, max=360)],render_kw={"placeholder": "description"})
    mass        = IntegerField("Mass (volume)", validators=[DataRequired()],render_kw={"placeholder": "mass (integer)"})
    price       = IntegerField("Price (uah)", validators=[DataRequired()],render_kw={"placeholder": "price (integer)"})
    image       = FileField('Image File', validators=[FileRequired(),FileAllowed(['jpg','jpeg','png'])],render_kw={"placeholder": "description"})
    submit      = SubmitField("Save")

class LogInForm(FlaskForm):
    email       = StringField("Email", [DataRequired(), Email(), Length(min=5, max=30)], render_kw={"placeholder": "name@gmail.com"})
    password    = PasswordField("Password", [DataRequired()],render_kw={"placeholder": "******"})
    submit      = SubmitField("Log in")

