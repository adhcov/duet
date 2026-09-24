
import base64
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="For My Love ❤️",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"
GALLERY = ASSETS / "gallery"
SONG = ASSETS / "song.mp3"

# ---------- Helpers ----------
def data_uri(path: Path) -> str:
    if not path.exists():
        return ""
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    raw = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{raw}"

def audio_data_uri(path: Path) -> str:
    if not path.exists():
        return ""
    raw = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:audio/mpeg;base64,{raw}"

# ---------- Styling ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Great+Vibes&display=swap');

.stApp {
    background:
        radial-gradient(circle at 20% 10%, rgba(255,220,232,.55), transparent 30%),
        radial-gradient(circle at 85% 15%, rgba(255,239,246,.8), transparent 30%),
        linear-gradient(145deg, #fff7fa 0%, #fff 45%, #fff0f5 100%);
    color: #4b2734;
}

.block-container {
    max-width: 820px;
    padding-top: 3rem;
    padding-bottom: 4rem;
}

h1, h2, h3, p, label, div {
    font-family: 'Cormorant Garamond', Georgia, serif;
}

.title {
    text-align:center;
    font-family:'Great Vibes', cursive !important;
    font-size: clamp(3.3rem, 11vw, 6.5rem);
    color:#a94c70;
    line-height:1;
    margin-bottom:.25rem;
}

.subtitle {
    text-align:center;
    font-size:1.35rem;
    color:#805264;
    margin-bottom:2.2rem;
}

.question-card {
    background: rgba(255,255,255,.76);
    border:1px solid rgba(193,113,143,.18);
    border-radius:28px;
    padding:2rem 1.5rem 1.2rem;
    box-shadow:0 18px 60px rgba(130,57,87,.12);
    backdrop-filter: blur(12px);
}

.small-note {
    text-align:center;
    color:#9b6a7b;
    font-size:1rem;
    margin-top:1.3rem;
}

div.stButton > button {
    width:100%;
    border-radius:18px;
    border:1px solid #e8b6c9;
    background:rgba(255,247,250,.95);
    color:#633447;
    font-size:1.2rem;
    padding:.75rem 1rem;
    transition:.2s ease;
}

div.stButton > button:hover {
    border-color:#c56c8e;
    color:#a43e68;
    transform:translateY(-1px);
    box-shadow:0 8px 24px rgba(168,74,111,.13);
}

.result {
    text-align:center;
    padding:1rem;
    font-size:1.25rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">For My Love</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">A little memory from two years ago… 💗</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="question-card">', unsafe_allow_html=True)
st.markdown(
    '<h2 style="text-align:center;">Do you remember this? 🌷</h2>'
    '<p style="text-align:center;font-size:1.25rem;">'
    'Which song did you sing for me the first time?</p>',
    unsafe_allow_html=True
)

options = [
    "Pandetho Rajyathe Rajakumariykku",
    "Perilarajyathe Rajakumari",
    "Ranjha",
]

answer = st.radio(
    "Choose one:",
    options,
    index=None,
    label_visibility="collapsed",
)

if st.button("Open the memory 💌", use_container_width=True):
    st.session_state["answered"] = True
    st.session_state["correct"] = answer == "Perilarajyathe Rajakumari"

st.markdown("</div>", unsafe_allow_html=True)

if st.session_state.get("answered"):
    if st.session_state.get("correct"):
        st.success("You remembered it. ❤️")

        flower = data_uri(ASSETS / "lilies.png")
        photos = []
        if GALLERY.exists() and GALLERY.is_dir():
            for p in sorted(GALLERY.iterdir()):
                if p.is_file() and p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}:
                    uri = data_uri(p)
                    if uri:
                        photos.append(uri)

        audio = audio_data_uri(SONG)

        # Everything below the answer is intentionally one interactive HTML
        # experience, so clicking the flower is a real browser gesture that
        # can start the audio.
        component_html = f"""
<!doctype html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {{ box-sizing:border-box; }}
html,body {{
  margin:0; padding:0; min-height:100%;
  background:transparent;
  overflow-x:hidden;
  font-family:Georgia, serif;
  color:#5b3041;
}}
.scene {{
  min-height:760px;
  position:relative;
  overflow:hidden;
  border-radius:30px;
  background:
    radial-gradient(circle at 50% 45%, rgba(255,255,255,.98), rgba(255,237,245,.92) 58%, rgba(255,216,231,.75));
  box-shadow:0 18px 60px rgba(130,57,87,.16);
  padding:30px 18px 42px;
}}
.bokeh {{
  position:absolute; inset:-20px;
  overflow:hidden; pointer-events:none;
}}
.dot {{
  position:absolute; border-radius:50%;
  background:rgba(255,190,214,.45);
  filter:blur(3px);
  box-shadow:0 0 25px rgba(255,157,193,.7);
  animation:float 7s ease-in-out infinite;
}}
@keyframes float {{
  0%,100% {{ transform:translateY(0) scale(1); opacity:.45; }}
  50% {{ transform:translateY(-30px) scale(1.08); opacity:.85; }}
}}
.content {{
  position:relative; z-index:2;
  display:flex; flex-direction:column; align-items:center;
  text-align:center;
}}
.small {{
  letter-spacing:.15em; text-transform:uppercase;
  font-size:.75rem; color:#a06a7e;
}}
.love {{
  font-family:'Brush Script MT','Segoe Script',cursive;
  font-size:clamp(2.7rem,10vw,5rem);
  line-height:1.05;
  color:#a8436a;
  margin:8px 0 4px;
}}
.sub {{
  font-size:1.25rem;
  margin:0 0 20px;
  color:#754256;
}}
.flower-wrap {{
  position:relative;
  width:min(430px,88vw);
  cursor:pointer;
  transition:transform .3s ease;
  filter:drop-shadow(0 16px 18px rgba(151,66,103,.18));
}}
.flower-wrap:hover {{ transform:scale(1.025); }}
.flower-wrap::before {{
  content:"";
  position:absolute; inset:8% 10%;
  border-radius:50%;
  background:rgba(255,188,216,.3);
  filter:blur(28px);
  z-index:-1;
}}
.flower {{
  width:100%; height:auto; display:block;
}}
.tap {{
  margin-top:-8px;
  font-size:1.05rem;
  color:#9b5a71;
  animation:pulse 1.7s infinite;
}}
@keyframes pulse {{ 50% {{ opacity:.48; transform:scale(.98); }} }}
.memory {{
  display:none;
  width:min(720px,96%);
  margin-top:18px;
  animation:rise .9s ease both;
}}
@keyframes rise {{
  from {{ opacity:0; transform:translateY(28px); }}
  to {{ opacity:1; transform:translateY(0); }}
}}
.message {{
  font-family:'Brush Script MT','Segoe Script',cursive;
  font-size:clamp(2.1rem,7vw,3.8rem);
  color:#a8436a;
  line-height:1.05;
  margin:8px 0 22px;
}}
.divider {{
  width:80px; height:1px; background:#d99bb1; margin:12px auto 24px;
}}
.gallery {{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(210px,1fr));
  gap:14px;
}}
.gallery img {{
  width:100%; height:auto; max-height:500px; object-fit:cover;
  border-radius:20px;
  box-shadow:0 10px 30px rgba(85,37,57,.15);
}}
.hint {{ font-size:.95rem; color:#936377; margin-top:18px; }}
audio {{ width:min(680px,96%); margin:8px auto 22px; }}
.missing {{
  padding:18px; border-radius:16px;
  background:rgba(255,255,255,.72);
  color:#7a4258; font-size:1rem;
}}
</style>
</head>
<body>
<div class="scene">
  <div class="bokeh">
    <span class="dot" style="width:70px;height:70px;left:7%;top:16%;animation-delay:.4s"></span>
    <span class="dot" style="width:36px;height:36px;left:23%;top:65%;animation-delay:1.2s"></span>
    <span class="dot" style="width:85px;height:85px;right:7%;top:10%;animation-delay:2s"></span>
    <span class="dot" style="width:46px;height:46px;right:18%;top:57%;animation-delay:3s"></span>
    <span class="dot" style="width:28px;height:28px;left:45%;top:9%;animation-delay:1.8s"></span>
    <span class="dot" style="width:58px;height:58px;left:2%;top:43%;animation-delay:2.7s"></span>
    <span class="dot" style="width:32px;height:32px;right:38%;top:70%;animation-delay:3.7s"></span>
  </div>

  <div class="content">
    <div class="small">For the girl who sang it for me</div>
    <div class="love">My Love &amp; My Wife</div>
    <div class="sub">There is one more little surprise for you…</div>

    <div class="flower-wrap" id="flower" title="Tap the flowers">
      <img class="flower" src="{flower}" alt="Pink lilies">
    </div>
    <div class="tap" id="tapText">Tap the flowers 🌸</div>

    <div class="memory" id="memory">
      <div class="message">This is for you, my love &amp; my wife. ❤️</div>
      <div class="divider"></div>
      {f'<audio id="song" src="{audio}" controls></audio>' if audio else '<div class="missing">🎵 Add your song as <b>assets/song.mp3</b> in the GitHub project to enable the music.</div>'}
      <div class="gallery">
        {''.join(f'<img src="{p}" alt="Our memory">' for p in photos)}
      </div>
      <div class="hint">Two voices, one memory. And hopefully many more years. ♾️❤️</div>
    </div>
  </div>
</div>

<script>
const flower = document.getElementById('flower');
const memory = document.getElementById('memory');
const tapText = document.getElementById('tapText');
const song = document.getElementById('song');

flower.addEventListener('click', async () => {{
  memory.style.display = 'block';
  tapText.textContent = 'Our little memory ❤️';
  if (song) {{
    try {{
      song.volume = 0.9;
      await song.play();
    }} catch (e) {{
      // Some browsers still require the audio control to be pressed.
      // The visible player remains available as a fallback.
    }}
  }}
  memory.scrollIntoView({{behavior:'smooth', block:'start'}});
}});
</script>
</body>
</html>
"""
        components.html(component_html, height=820, scrolling=False)

    else:
        st.error("Almost! 😄 Try to remember the song you sang for me…")
        st.markdown(
            '<div class="result">I think your heart knows the answer. 💗</div>',
            unsafe_allow_html=True
        )

st.markdown(
    '<div class="small-note">Made with love, for one very special person. 🌷</div>',
    unsafe_allow_html=True
)
