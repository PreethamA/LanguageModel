from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def count_words_chars_numbers(text):
    word_count = len(text.split())
    char_count = len(text)
    num_count = len(re.findall(r'\d+', text))
    return word_count, char_count, num_count

@app.route('/analyze', methods=['POST'])
def analyze_document():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    content = file.read().decode("latin-1")

    word_count, char_count, num_count = count_words_chars_numbers(content)

    result = {
        'word_count': word_count,
        'char_count': char_count,
        'num_count': num_count
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

