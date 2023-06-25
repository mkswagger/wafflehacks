from flask import Flask, request, jsonify
from flask_cors import CORS

from text_classifier import perform_sentiment_analysis

app = Flask(__name__)

# Allow CORS for all domains on all routes
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/check_text', methods=['POST'])
def check_text():
    data = request.get_json()
    text = data['text']

    # split text into sentences
    sentences = text.split('.')

    # check each sentence
    result = []
    for sentence in sentences:
        result.append(check_text_function(sentence))

    
    return jsonify({'result': result})

def check_text_function(text):
    # Implement your text checking logic here
    if 'bad' in text:
        return 'Contains bad word'
    return 'Text is clean'

if __name__ == '__main__':
    app.run(debug=True)
