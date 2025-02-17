import azure.cognitiveservices.speech as speechsdk

# Set up your Azure Speech API credentials
subscription_key = "1wloZLPX3hLZaAk9cwWhW2XVv2BVgYCJUHu0DpoGb4z6jWEW3pw4JQQJ99BBACYeBjFXJ3w3AAAYACOGpNxi"
region = "eastus"  # e.g., "eastus"

def text_to_speech(text, output_audio_file="Intro1.wav"):
    # Set up the speech configuration
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
    
    # Choose a male voice (you can change the voice to others if you prefer)
    speech_config.speech_synthesis_voice_name = "en-US-GuyNeural"  # Male voice
    
    # Set the output audio configuration (e.g., save as a WAV file)
    audio_config = speechsdk.audio.AudioOutputConfig(filename=output_audio_file)

    # Set up the synthesizer
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # Synthesize the text to speech
    result = synthesizer.speak_text_async(text).get()

    # Check result and handle errors
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Successfully synthesized the speech.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        # Handle cancellation of speech synthesis
        cancellation_details = result.cancellation_details
        print(f"Speech synthesis canceled: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print(f"Error details: {cancellation_details.error_details}")
    else:
        print(f"Unexpected result: {result.reason}")

# Example: Convert some text to speech
if __name__ == "__main__":
    text = "Welcome to Tech Arch Lab!"
    text_to_speech(text)