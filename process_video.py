import os
import whisper
import csv

# 1. Load Whisper model and transcribe
model = whisper.load_model("base")
result = model.transcribe("mechanic_video.mp4")

# 2. (Optional) Extract frames - if you want to do it here or do it separately
# You can import and call your frame extraction function/script here

# 3. Match frames to transcript and print + save CSV
fps = 30  # Adjust this if your frame extraction used a different FPS
frames_folder = "frames"

segments = result['segments']
frame_files = sorted(os.listdir(frames_folder))

with open('frame_transcript.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['frame_file', 'time_sec', 'transcript'])

    for frame_file in frame_files:
        frame_num = int(''.join(filter(str.isdigit, frame_file)))
        frame_time = frame_num / fps

        matching_text = ""
        for seg in segments:
            if seg['start'] <= frame_time <= seg['end']:
                matching_text = seg['text']
                break

        print(f"Frame: {frame_file}, Time: {frame_time:.2f}s, Transcript: {matching_text}")
        writer.writerow([frame_file, f"{frame_time:.2f}", matching_text])
