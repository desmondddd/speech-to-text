# %% convert m4a to wav
from pydub import AudioSegment

source_audio_file_path = "2023_05_27_interview_on_system.m4a"

# convert m4a audio to wav using pydub:
print('Converting m4a into wav ...')
audio = AudioSegment.from_file(source_audio_file_path, format="m4a")
audio.export(f"output.wav", format="wav")
print('------------------- Done -------------------')



# %% convert wav to text
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()


with sr.AudioFile('output.wav') as speech:
    audio_data = r.listen(speech)

    text = r.recognize_whisper(audio_data, language='en')
    print('Converting audio transcripts into text ...')
    with open("output.txt", "w",) as text_file:
        text_file.write(text)
    print('------------------- Done -------------------')

