from emotion_detector import detect_emotion
from music_player import play_music

def main():
    emotion = detect_emotion()
    if emotion:
        play_music(emotion)

if __name__ == "__main__":
    main()
