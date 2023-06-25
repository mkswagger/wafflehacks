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

    if text is None:
        return jsonify({'error': 'No text provided'})

    # split text into sentences
    sentences = text.split('.')

    # check each sentence
    result = []
    for sentence in sentences:
        sentence = sentence.strip()
        # if sentence is too long, split it into smaller sentences
        if len(sentence) > 15:
            bad = False
            while len(sentence) > 15:
                if perform_sentiment_analysis(sentence[:15]) == "offensive":
                    bad = True
                    break

                sentence = sentence[15:]
            if perform_sentiment_analysis(sentence) == "offensive":
                bad = True
            result.append("offensive" if bad else "not offensive")

        else:
            result.append(perform_sentiment_analysis(sentence))

    
    return jsonify({'result': result})



if __name__ == '__main__':
    app.run(debug=True)
