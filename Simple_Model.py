import streamlit as st
import whisper
import re
from transformers import pipeline

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Meeting Minutes Generator")
st.title("🎙️ AI Meeting Minutes Generator")

st.write(
    "Upload a meeting audio file (.wav or .mp3) to generate "
    "an automatic meeting summary."
)

# ---------------- LOAD MODELS ----------------
@st.cache_resource
def load_models():
    whisper_model = whisper.load_model("small")
    summarizer_model = pipeline(
        "summarization",
        model="facebook/bart-large-cnn"
    )
    return whisper_model, summarizer_model


# ---------------- TEXT CLEANING ----------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# ---------------- FILE UPLOAD ----------------
uploaded_audio = st.file_uploader(
    "Upload meeting audio",
    type=["wav", "mp3"]
)

if uploaded_audio is not None:
    st.audio(uploaded_audio)

    if st.button("Generate Meeting Summary"):
        with st.spinner("Loading models..."):
            whisper_model, summarizer = load_models()

        # Save uploaded file
        audio_path = "uploaded_meeting_audio.wav"
        with open(audio_path, "wb") as f:
            f.write(uploaded_audio.read())

        # ---------------- TRANSCRIPTION ----------------
        with st.spinner("Transcribing audio..."):
            result = whisper_model.transcribe(audio_path)
            transcript = result["text"]

        st.subheader("📝 Meeting Transcript")
        st.write(transcript)

        # ---------------- CLEAN TEXT ----------------
        cleaned_transcript = clean_text(transcript)

        # ---------------- SUMMARIZATION ----------------
        with st.spinner("Generating summary..."):
            summary = summarizer(
                cleaned_transcript,
                max_length=100,
                min_length=40,
                do_sample=False
            )

        st.subheader("📌 Meeting Summary")
        st.success(summary[0]["summary_text"])