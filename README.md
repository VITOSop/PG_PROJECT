# 🧠 AI Meeting Minutes Generator

An end-to-end AI system that converts raw meeting audio into structured meeting minutes, including speaker diarization, transcription, summarization, bullet points, and action items.

## 🚀 Features
- 🎧 Upload meeting audio (`.wav`)
- 🔊 Speaker diarization (who spoke when)
- 📝 Speaker-wise transcription using OpenAI Whisper
- 📄 Automatic meeting summary
- 🤖 AI-generated bullet points
- ✅ Action item extraction (Task | Owner | Deadline)
- 📊 Token usage metrics
- 🖥️ Interactive Streamlit UI

## 🧩 Tech Stack
- **UI:** Streamlit
- **Speech-to-Text:** OpenAI Whisper
- **Speaker Diarization:** PyAnnote Audio
- **Summarization:** BART (`facebook/bart-large-cnn`)
- **LLM Reasoning:** Mistral-7B-Instruct
- **Audio Processing:** PyDub
- **Model Hub:** Hugging Face
- **Language:** Python

