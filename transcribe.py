import whisper

# Load the model
model = whisper.load_model("base")  # You can also try "small" or "medium" if you want better accuracy

# Transcribe the audio file
result = model.transcribe("mechanic_audio.mp4")

# Print the text
print(result["text"])
with open("mechanic_audio_transcript.txt", "w") as f:
    f.write(result["text"])
