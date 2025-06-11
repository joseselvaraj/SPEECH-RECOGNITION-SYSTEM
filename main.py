import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.AudioFile("audio.wav") as source:
    print("Listening...")
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio)
    print("Text Output:\n", text)

    with open("output.txt", "w") as file:
        file.write(text)
    print("\n✅ Transcription saved to output.txt")

except sr.UnknownValueError:
    print("❌ Could not understand the audio.")
except sr.RequestError as e:
    print(f"❌ Request error: {e}")
