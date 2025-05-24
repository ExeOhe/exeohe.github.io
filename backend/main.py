from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/skill/webdesign')
def skill_webdesign():
    return render_template('html/skill.webdesign.html')

@app.route('/skill/js')
def skill_js():
    return render_template('html/skill.js.html')

@app.route('/skill/python')
def skill_python():
    return render_template('html/skill.python.html')

# Import and register AI/chatbot route
import main2  # This will add /chat to the same app

if __name__ == "__main__":
    app.run(debug=True, port=5500)

