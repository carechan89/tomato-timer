from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

# Flask-WTF requires an encryption key which can be any string
app.config['SECRET_KEY'] = 'ySaMndXKbC6xvYP13LJ66ZetQWm3ivlP'

# Flask-Bootstrap requires this line
Bootstrap(app)

# Create forms here
class TimeForm(FlaskForm):
    worktime = IntegerField('Enter work time', validators=[DataRequired()])
    breaktime = IntegerField('Enter break time', validators=[DataRequired()])
    submit = SubmitField('Submit preferences')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TimeForm()
    message = ''
    if form.validate_on_submit():
        worktime = form.worktime.data
        breaktime = form.breaktime.data
        # TODO: need to do something here, maybe kick off the timer?
    else:
        message = 'Something went wrong. Please try again.'
    return render_template('index.html', worktime=worktime, breaktime=breaktime, message=message)
