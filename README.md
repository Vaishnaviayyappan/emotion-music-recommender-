# Emotion-Based Music Recommender

This project detects a user's emotion using facial expression analysis and plays a matching song using YouTube audio streams.

## Features

- Real-time emotion detection via webcam using DeepFace
- Emotion-to-music mapping via YouTube
- Audio streaming with pafy and VLC
- Simple CLI-based experience

## Installation

```bash
git clone https://github.com/yourusername/emotion-music-recommender.git
cd emotion-music-recommender
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Notes

If `youtube-dl` fails, use:

```bash
pip install yt-dlp
pip install git+https://github.com/mps-youtube/pafy
```

Then update `pafy` backend:

```python
import pafy
pafy.set_backend("internal")
```

## License

MIT License
