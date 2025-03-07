# Lab 7a
import wave

# Open the WAV file in read mode
wav_file = wave.open(r"D:\Kunaa_____l\multi-media\lab7\example.wav", "r")
# Get the parameters of the WAV file
num_channels = wav_file.getnchannels()  # Corrected method
sample_width = wav_file.getsampwidth()
sample_rate = wav_file.getframerate()
num_samples = wav_file.getnframes()

# Close the WAV file
wav_file.close()

# Print the parameters
print("Number of channels: ", num_channels)
print("Sampling width (bit depth): ", sample_width)
print("Sampling rate: ", sample_rate)
print("Number of samples: ", num_samples)
