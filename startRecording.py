import pyaudio
import pyttsx3
import wave

# set up the audio parameters
audio_format = pyaudio.paInt16
channels = 1
sample_rate = 44100
chunk = 4096
record_seconds = 10
usrQuestionFile = "userQuestion.wav"

# initialize PyAudio
engine = pyttsx3.init()
audio = pyaudio.PyAudio()

# readying recording
engine.say("What can I help you with. Press x when you are done")
engine.runAndWait()
# must stop before using pyaudio
# gTTS seems to collide with pyaudio
engine.stop()

# ---Record Function---#

# open the stream
stream = audio.open(format=audio_format, channels=channels,
                    rate=sample_rate, input=True,
                    frames_per_buffer=chunk)

while True:
    frames = []
    for i in range(0, int(sample_rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)
    userIntent = input()
    if userIntent == "x":
        break
# stop recording
print("recording terminated")
stream.stop_stream()
stream.close()
audio.terminate()

# write the recorded data to a WAV file
wf = wave.open(usrQuestionFile, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(audio.get_sample_size(audio_format))
wf.setframerate(sample_rate)
wf.writeframes(b''.join(frames))
wf.close()


"""def record():
    # open the stream
    stream = audio.open(format=audio_format, channels=channels,
                        rate=sample_rate, input=True,
                        frames_per_buffer=chunk)

    while True:
        frames = []
        for i in range(0, int(sample_rate / chunk * record_seconds)):
            data = stream.read(chunk)
            frames.append(data)
        userIntent = input()
        if userIntent == "x":
            break

    # stop recording
    print("recording terminated")
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # write the recorded data to a WAV file
    wf = wave.open(file_name, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(audio_format))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()"""
