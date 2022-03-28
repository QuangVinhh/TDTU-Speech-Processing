#-----import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

#-----Sampling frequency
freq = 44100
  
#-----Recording duration
duration = 2
  
#-----Start recorder with the given values of duration and sample frequency
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
  
#-----Record audio for the given number of seconds
sd.wait()
  
#-----This will convert the NumPy array to an audio file with the given sampling frequency
# write("recording0.wav", freq, recording)
  
#-----Convert the NumPy array to audio file
wv.write("./records/oh/oh_15_51900781.wav", recording, freq, sampwidth=1)

#-----Tools record Update-----#

# seconds = 1  # Duration of recording

# list = ['one','two','three','four','five','six','seven','eight','nine','zero','oh']

# for i in range(11):
#     for j in range(1,16):
#         fileName = list[i]+'_'+str(j)+'_51900741.wav'
#         print(fileName)

#         myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
#         sd.wait()  # Wait until recording is finished


#         write(fileName, fs, myrecording)  # Save as WAV file 
