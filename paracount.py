from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def count_paragraphs_lines_words_chars_numbers(text):
    paragraphs = text.split('\n\n')
    paragraph_count = len(paragraphs)
    paragraph_info = []
    
    for paragraph in paragraphs:
        lines = paragraph.split('\n')
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)
        num_count = sum(len(re.findall(r'\d+', line)) for line in lines)
        paragraph_info.append({
            'line_count': line_count,
            'word_count': word_count,
            'char_count': char_count,
            'num_count': num_count
        })
        
    return paragraph_count, paragraph_info

@app.route('/analyze', methods=['POST'])
def analyze_document():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        content = file.read().decode("utf-8")
    except UnicodeDecodeError:
        try:
            content = file.read().decode("latin-1")
        except UnicodeDecodeError:
            return jsonify({'error': 'Failed to decode file with UTF-8 and latin-1 encoding'}), 400
	
    paragraph_count, paragraph_info = count_paragraphs_lines_words_chars_numbers(content)

    result = {
        'paragraph_count': paragraph_count,
        'paragraphs': paragraph_info
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

