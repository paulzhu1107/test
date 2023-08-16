import os
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

music_extensions = ['.mp3', '.wav', '.flac']  # 音乐文件扩展名

def play_music_with_potplayer(file_path):
    potplayer_path = r"C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe"
    subprocess.Popen([potplayer_path, file_path])

def get_music_files(directory):
    music_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            _, extension = os.path.splitext(file)
            if extension.lower() in music_extensions:
                music_files.append(file)
    return music_files

@app.route('/play_music', methods=['POST'])
def play_music():
    data = request.json
    file_path = data.get('file_path')

    if not file_path:
        return jsonify({'error': 'Missing file_path'}), 400

    play_music_with_potplayer(file_path)
    return jsonify({'message': 'Music playback initiated'})

if __name__ == '__main__':
    app.run(debug=True)
