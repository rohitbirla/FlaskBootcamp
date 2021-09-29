from flask import Flask,render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField,BooleanField,DateField,DateTimeField,TextAreaField,TextField,RadioField,SubmitField
from wtforms.fields.core import SelectField
from wtforms.validators import DataRequired

app =Flask(__name__)

app.config['SECRET_KEY'] ='mykey'

class InfoForm(FlaskForm):
    breed =StringField('What breed are you?',validators=[DataRequired()])
    neutered = BooleanField("Have you been neutered?")
    mood = RadioField('Please choose your mood:',choices=[('mood_one','Happy'),('mood_two','Excited')])
    food_choice = SelectField(u'Pick your favorite food:',choices=[('chi','chicken'),('bf','Beef'),('fish','Fish')])
    feedback = TextAreaField()
    submit = SubmitField('submit')


@app.route('/',methods =['GET','POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))
    return render_template('01index.html',form=form)        


@app.route('/thankyou')
def thankyou():
    return render_template('01thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)


