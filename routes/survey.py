from services.survey_service import get_intro_text
from flask import render_template, request, redirect, url_for, flash, Blueprint
from forms.health_form import HealthSurveyForm
from models.health_survey import HealthSurvey
from database_init import db
from services.survey_service import generate_health_prompt
from services.gemini_service import get_health_advice_from_gemini

survey_bp = Blueprint("survey", __name__, url_prefix="/survey")

@survey_bp.route("/start", methods=["GET", "POST"])
def start():
    form = HealthSurveyForm()
    if form.validate_on_submit():
        survey = HealthSurvey(
            age=form.age.data,
            gender=form.gender.data,
            has_chronic_disease=form.has_chronic_disease.data,
            smoking=form.smoking.data,
        )
        db.session.add(survey)
        db.session.commit()
        flash("Khảo sát của bạn đã được ghi nhận!", "success")
        return redirect(url_for("survey.result", survey_id=survey.id))
    return render_template("survey/start.html", form=form)

@survey_bp.route("/result/<int:survey_id>")
def result(survey_id):
    survey = HealthSurvey.query.get_or_404(survey_id)

    prompt = generate_health_prompt(survey)
    ai_response = get_health_advice_from_gemini(prompt)

    return render_template(
        "survey/result.html",
        survey=survey,
        prompt=prompt,
        ai_response=ai_response
    )