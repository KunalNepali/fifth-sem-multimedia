import numpy as np
import matplotlib.pyplot as plt

# Parameters for the sine wave
frequency = 3  # Hz
amplitude = 1  # Amplitude
phase = 0      # Phase
sampling_rate = 6  # Nyquist theorem: Sampling rate should be >= 2 * frequency
time = np.arange(0, 10, 1/sampling_rate)  # Time vector from 0 to 10 seconds

# Compute sine wave values
sine_wave_values = amplitude * np.sin(2 * np.pi * frequency * time + phase)

# Plot the sine wave
plt.plot(time, sine_wave_values, label="Sine Wave (3 Hz)", color='b')
plt.scatter(time, sine_wave_values, color='r', label="Sampled Points", zorder=5)

# Label the plot
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Sine Wave with 6Hz Sampling Rate (Nyquist Theorem)")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
