from flask import Flask
from flask.templating import render_template
from flask import request
from flask.json import jsonify
from openai import OpenAI

# Put your OpenAI API key here
client = OpenAI(api_key="")


# To make database related code work, go to database.py to add
# MySQL connection string and uncomment the code below
#from database import database

jobs_1 = [
    {'id': 1, 'title': 'Software Developer', 'location': 'Calgary', 'salary': 100000},
    {'id': 2, 'title': 'Data Analyst', 'location': 'Toronto', 'salary': 80000}]



# App starts here

app = Flask(__name__)

home_title = 'ENSF607/608 Planning a Vacation'

# 1. consider change face icon
@app.route('/')
def hello_world():
  # to use database realted code, follow the instructions on line 11
  #jobs = database().load_jobs_dicts_from_db()
  return render_template('home.html', jobs=jobs_1, title=home_title)


@app.route('/plan', methods=['POST'])
def plan():
    country = request.form['country']
    vacation_type = request.form['vacation_type']

    # New ChatGPT API prompt
    prompt = f"Suggest a {vacation_type} vacation in {country}. Provide suggestions of things to do."

    # Use ChatCompletion (ChatGPT API) for the new interface
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a vacation planner."},
        {"role": "user", "content": prompt}
    ])
    content = response.choices[0].message.content
    vacation_plan = content.strip() if content else "No vacation plan available."

    return render_template('plan.html', vacation_plan=vacation_plan)


# Test run
print(__name__)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=3000)
