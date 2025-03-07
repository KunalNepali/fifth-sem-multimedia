import numpy as np
import matplotlib.pyplot as plt

# Define sine wave parameters
frequency = 3  # Hz
amplitude = 1  # Amplitude of the sine wave
phase = 0      # Phase shift
sampling_rate = 2  # Hz (Sampling rate)
time = np.arange(0, 10, 1/sampling_rate)  # From 0 to 10 seconds with 2Hz sampling

# Compute sine wave values
sine_wave_values = amplitude * np.sin(2 * np.pi * frequency * time + phase)

# Plot the sampled points
plt.scatter(time, sine_wave_values, color='red', label="Samples")
plt.plot(time, sine_wave_values, linestyle='dashed', color='blue', label="Sine Wave")

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Sine Wave with 2Hz Sampling Rate")
plt.legend()
plt.show()
