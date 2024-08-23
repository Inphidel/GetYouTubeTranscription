from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
import json

def get_video_transcript(url):
    try:
        # Fetch video details
        yt = YouTube(url)
        
        # Check if there's a transcript available
        try:
            transcript = YouTubeTranscriptApi.get_transcript(yt.video_id)
            # Convert list of dicts to a string
            transcript_text = ' '.join([entry['text'] for entry in transcript])
            return transcript_text
        except YouTubeTranscriptApi.NoTranscriptFound:
            print("No transcript available for this video.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def save_to_file(text, filename="transcript.txt"):
    if text:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Transcript saved to {filename}")
    else:
        print("No text to save.")

# Example usage
video_url = input("Enter the YouTube video URL: ")
transcript = get_video_transcript(video_url)
save_to_file(transcript)
