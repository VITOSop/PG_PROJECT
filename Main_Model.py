import streamlit as st
import tempfile
import os
from moviepy.editor import VideoFileClip

# ===============================
# Page config
# ===============================
st.set_page_config(
    page_title="AI Meeting Minutes Generator",
    layout="centered"
)

st.title("🎥 AI Meeting Minutes Generator")
st.write(
    "Upload a meeting video and receive speaker-wise transcripts, "
    "summary, and action items automatically."
)

# ===============================
# Video upload
# ===============================
video_file = st.file_uploader(
    "Upload meeting video",
    type=["mp4", "mov", "mkv"]
)

def extract_audio(video_path):
    clip = VideoFileClip(video_path)
    audio_path = video_path.replace(".mp4", ".wav")
    clip.audio.write_audiofile(audio_path)
    return audio_path

# ===============================
# Main pipeline
# ===============================
if video_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
        tmp.write(video_file.read())
        video_path = tmp.name

    st.video(video_path)

    if st.button("🚀 Generate Meeting Minutes"):
        with st.spinner("Processing video and extracting insights..."):

            # -------------------------------
            # 1. Extract audio
            # -------------------------------
            audio_path = extract_audio(video_path)

            st.success("Audio extracted successfully")

            # -------------------------------
            # 2. CALL YOUR EXISTING FUNCTIONS
            # -------------------------------
            """
            Replace below with your notebook functions:

            diarization(audio_path)
            transcription(diarized_segments)
            summary = summarize(text)
            action_items = agentic_ai(summary)
            """

            # Example placeholders
            speaker_transcript = """
            Speaker 1: Project timeline discussed.
            Speaker 2: Deployment planned next week.
            """

            summary = """
            The meeting focused on finalizing the project timeline and deployment plan.
            """

            action_items = """
            • Prepare deployment checklist – John – Due Friday
            • Final QA review – Team – Due Thursday
            """

            # -------------------------------
            # 3. Display results
            # -------------------------------
            st.subheader("🗣 Speaker-wise Transcript")
            st.text_area("", speaker_transcript, height=200)

            st.subheader("📌 Meeting Summary")
            st.text_area("", summary, height=150)

            st.subheader("✅ Action Items")
            st.text_area("", action_items, height=150)

            st.success("Meeting minutes generated successfully!")
