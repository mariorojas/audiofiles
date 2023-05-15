# Programmatically podcast creation 

**INSTALLATION COMMANDS**

```
git clone https://github.com/mariorojas/audiofiles.git
cd audiofiles/
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

# install ffmpeg for mp3 processing
brew install ffmpeg
```

Please read [pydub documentation](https://github.com/jiaaro/pydub) in case of file processing errors.

To create an audio file, run the following:

```
python main.py
# output: podcast.mp3...
```

TO-DO:
- Music loop when voice is larger than music
- Multiple voices for conversational podcasts