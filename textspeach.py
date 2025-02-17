from gtts import gTTS

# Function to save text as speech
def save_text_to_speech(text, filename="output.mp3"):
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(filename)
    print(f"Speech saved as {filename}")

# Example text
text = "Welcome to our amazing YouTube Shorts! Enjoy this short video."

# Save speech as an audio file
save_text_to_speech(text, "shorts_audio.mp3")
