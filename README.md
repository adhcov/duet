# 💗 For My Love — Song Memory Website

A small romantic Streamlit website for a long-distance relationship.

## What it does

1. She sees the question: **Which song did you sing for me the first time?**
2. Options:
   - Pandetho Rajyathe Rajakumariykku
   - Perilarajyathe Rajakumari
   - Ranjha
3. The correct answer is **Perilarajyathe Rajakumari**.
4. After the correct answer, a pink-lily/bokeh surprise appears.
5. She clicks the lilies.
6. The click starts your song (when `assets/song.mp3` has been added) and reveals the photo gallery.
7. The supplied couple photo is already included.

## Add your song

Put your audio file here:

```text
assets/song.mp3
```

MP3 is recommended.

## Add your other pictures

Put JPG/PNG/WebP photos in:

```text
assets/gallery/
```

You can keep the supplied `our_photo.png` or replace it.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Create a GitHub repository.
2. Upload:
   - `app.py`
   - `requirements.txt`
   - `assets/lilies.png`
   - `assets/song.mp3`
   - all your photos inside `assets/gallery/`
3. Go to Streamlit Community Cloud and create a new app from the GitHub repository.
4. Select `app.py` as the main file.
5. Deploy.
6. Send her the generated Streamlit link.

### Important
Do not put private information, passwords, API keys, or anything sensitive in the repository.

### Browser audio note
The website waits for her to **click the flowers** before calling `audio.play()`. This is intentional because modern browsers commonly block audio that starts without a user gesture. If a particular browser still blocks playback, the visible audio player can be pressed manually.
