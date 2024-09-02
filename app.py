from flask import Flask, render_template, request, jsonify, send_file
import random
import os
from gtts import gTTS

app = Flask(__name__)

colors = ['Red', 'Green', 'Blue', 'Yellow']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_test', methods=['POST'])
def start_test():
    random.shuffle(colors)
    return jsonify({'colors': colors})

@app.route('/speak_color', methods=['POST'])
def speak_color():
    try:
        color = request.json['color']
        filename = f"static/{color}.mp3"
        tts = gTTS(text=color, lang='en')
        tts.save(filename)
        return send_file(filename, mimetype="audio/mpeg")
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
