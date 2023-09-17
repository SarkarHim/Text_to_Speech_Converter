from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert_text_to_speech():
    text = request.json['text']  # Use request.json to access the JSON data
    lang = request.json['lang']  # Get the language from the JSON data
    tts = gTTS(text, lang=lang)

    # Create the 'static' directory if it doesn't exist
    os.makedirs('File', exist_ok=True)

    savefile = 'File/Audio.mp3'
    tts.save(savefile)
    return send_file(savefile, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
