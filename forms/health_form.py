from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, BooleanField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class HealthSurveyForm(FlaskForm):
    age = IntegerField("Tuổi", validators=[InputRequired(), NumberRange(min=1, max=120)])
    gender = RadioField("Giới tính", choices=[('male', 'Nam'), ('female', 'Nữ')], validators=[InputRequired()])
    has_chronic_disease = BooleanField("Có bệnh nền")
    smoking = BooleanField("Có hút thuốc")
    submit = SubmitField("Gửi khảo sát")
