from flask import Flask, render_template, send_from_directory
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Run Flask Application
app = Flask(__name__)

#Define General Routes

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static', 'images'),
        'selfie.jpg',
        mimetype='image/jpeg'
    )

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/skill/webdev')
def skill_webdev():
    return render_template('html/skill.webdev.html')

@app.route('/skill/ai')
def skill_ai():
    return render_template('html/skill.ai.html')

@app.route('/skill/proglang')
def skill_proglang():
    return render_template('html/skill.proglang.html')



# Import and register AI/chatbot route
import main2  # This will add /chat to the same app

if __name__ == "__main__":
    app.run(debug=True, port=5500)

