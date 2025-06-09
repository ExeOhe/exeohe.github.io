from flask import Flask, render_template, send_from_directory
from flask_session import Session
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Run Flask Application
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SESSION_SECRET_KEY")
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

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

@app.route('/skill/blockchain')
def skill_blockchain():
    return render_template('html/skill.blockchain.html')

# Register AI/chatbot blueprint
from main2 import ai_bp
app.register_blueprint(ai_bp)

# This will ONLY Run Flask If Locally
# Keep this at the end
# to run locally with "python3 main.py" command

if __name__ == "__main__":
    app.run(debug=True, port=5000)
