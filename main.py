
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Sample data for Australian sayings and their Dutch translations
sayings = {
    "fair dinkum": "echt waar",
    "she'll be right": "komt goed",
    "no worries": "geen probleem",
    "barbie": "barbecue",
    "mate": "vriend"
}

# Main page route
@app.route('/')
def index():
    return render_template('index.html')

# Translation route
@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    saying = data['saying']
    
    # Translate the saying using the sample data
    translation = sayings.get(saying, "Sorry, I don't know that saying.")
    
    # Return the translation as JSON
    return jsonify({'translation': translation})

if __name__ == '__main__':
    app.run()
