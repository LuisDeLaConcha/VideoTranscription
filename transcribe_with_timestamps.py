import whisper

model = whisper.load_model("base")
result = model.transcribe("mechanic_video.mp4")  # Replace with your actual video/audio file path

# Print segments with timestamps
for segment in result['segments']:
    print(f"[{segment['start']:.2f} - {segment['end']:.2f}] {segment['text']}")
