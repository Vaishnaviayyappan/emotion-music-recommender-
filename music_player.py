import pafy
import vlc
import time
import json

def load_music_links():
    with open("youtube_links.json", "r") as f:
        return json.load(f)

def play_music(emotion):
    music_db = load_music_links()
    emotion = emotion.lower()
    if emotion not in music_db:
        print("No music found for this emotion.")
        return

    url = music_db[emotion]
    print(f"Playing music for {emotion} mood: {url}")
    video = pafy.new(url)
    best_audio = video.getbestaudio()
    player = vlc.MediaPlayer(best_audio.url)
    player.play()

    time.sleep(30)
    player.stop()
