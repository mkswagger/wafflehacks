from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check_text', methods=['POST'])
def check_text():
    data = request.get_json()
    # Perform text checking logic here
    text = data['text']
    result = check_text_function(text)
    return jsonify({'result': result})

def check_text_function(text):
    # Implement your text checking logic here
    if 'bad' in text:
        return 'Contains bad word'
    return 'Text is clean'

if __name__ == '__main__':
    app.run()
