import cv2
import whisper
import os

# Load Whisper model and transcribe
model = whisper.load_model("base")
result = model.transcribe("mechanic_video.mp4")

fps = 30  # Match your video's FPS
segments = result['segments']

# Open video file
video_path = "mechanic_video.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_num = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break  # End of video

    # Calculate current time in seconds
    frame_time = frame_num / fps

    # Find matching transcript text
    matching_text = ""
    for seg in segments:
        if seg['start'] <= frame_time <= seg['end']:
            matching_text = seg['text']
            break

    # Overlay the transcript text on the frame
    # Parameters: image, text, position, font, font scale, color, thickness, line type
    cv2.putText(frame, matching_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (0, 255, 0), 2, cv2.LINE_AA)

    # Show frame
    cv2.imshow('Video with Transcript', frame)

    # Press 'q' to quit early
    if cv2.waitKey(int(1000/fps)) & 0xFF == ord('q'):
        break

    frame_num += 1

cap.release()
cv2.destroyAllWindows()
