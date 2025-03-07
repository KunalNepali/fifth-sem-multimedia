# Lab 7b
import wave
import math

frequency = 440  # Hz (or keep 4400 if you like)
amplitude = 32767  # Max for 16-bit audio
phase = 0
duration = 1  # seconds
sample_rate = 44100
num_samples = int(sample_rate * duration)

with wave.open('sine_wave.wav', 'w') as file:
    file.setnchannels(1)  # Mono
    file.setsampwidth(2)  # 2 bytes = 16-bit
    file.setframerate(sample_rate)

    for i in range(num_samples):
        time = i / sample_rate
        sample = amplitude * math.sin(2 * math.pi * frequency * time + phase)
        sample_int = int(sample)
        sample_bytes = sample_int.to_bytes(2, byteorder='little', signed=True)
        file.writeframes(sample_bytes)
