from moviepy.editor import *
import sys


def extract_audio_from_video(video_path, audio_path="output_audio.wav"):
    """Extracts audio from a video and saves it as a WAV file."""
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python audio_extractor.py <video_path>")
        sys.exit(1)

    video_path = sys.argv[1]
    audio_path = os.path.splitext(video_path)[0] + "_audio.wav"

    extract_audio_from_video(video_path, audio_path)
    print(f"Audio extracted and saved to {audio_path}")
