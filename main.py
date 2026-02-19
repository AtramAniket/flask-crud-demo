from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, URL
from dotenv import load_dotenv
import csv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("APP_SECRET_KEY")
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired(message='Cafe name is required')])
    location = URLField('Location', validators=[DataRequired(message='URL is required'), URL(message='Enter a valid URL')])
    opening_time = SelectField('Open', choices=[('7:00AM', '7:00AM'), ('8:00AM', '8:00AM'), ('9:00AM', '9:00AM')])
    closing_time = SelectField('Close', choices=[('3:00PM', '3:00PM'), ('4:00PM', '4:00PM'), ('5:00PM', '5:00PM')])
    coffee = SelectField('Coffee', choices=[('☕️', '☕️'), ('☕️☕️', '☕️☕️'), ('☕️☕️☕️', '☕️☕️☕️'), ('☕️☕️☕️☕️', '☕️☕️☕️☕️'), ('☕️☕️☕️☕️☕️', '☕️☕️☕️☕️☕️')])
    wifi = SelectField('Wifi', choices=[('✘','✘'),('💪','💪'),('💪💪','💪💪'),('💪💪💪','💪💪💪'),('💪💪💪💪','💪💪💪💪'),('💪💪💪💪💪','💪💪💪💪💪')])
    power_sockets = SelectField('Power', choices=[('🔌','🔌'), ('🔌🔌','🔌🔌'), ('🔌🔌🔌','🔌🔌🔌'), ('🔌🔌🔌🔌','🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌','🔌🔌🔌🔌🔌')])
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add')
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
