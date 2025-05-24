from flask import Flask, render_template

app = Flask(__name__)

# Define a basic route
@app.route('/')
def home():
    return render_template('index.html')

#Defining Routes for different skills on index.html
@app.route('/skill/webdesign')
def skill_webdesign():
    return render_template('html/skill.webdesign.html')

@app.route('/skill/js')
def skill_js():
    return render_template('html/skill.js.html')

@app.route('/skill/python')
def skill_python():
    return render_template('html/skill.python.html')

#invoke hidden AI logic, 
# includes Local VS Public Application Server Op's
# defeats issue with Flask not being able to run in production mode
# pull requests wont affect server / no manual adjustments needed
# and no need to run the server in production mode

try:
    from main2 import run_app
    run_app()
except ImportError:
    print("Application logic is hidden or missing.")

