import numpy as np
import matplotlib.pyplot as plt

# Define sine wave parameters
frequency = 3  # Hz
amplitude = 1
phase = 0
interval = 0.3  # Sampling interval
samples = 10  # Number of samples
time_samples = np.arange(0, samples * interval, interval)

# Compute sine wave values
sine_wave_values = amplitude * np.sin(2 * np.pi * frequency * time_samples + phase)

# Plot samples
plt.scatter(time_samples, sine_wave_values, color='red', label="Samples")
plt.plot(time_samples, sine_wave_values, linestyle='dashed', color='blue', label="Sine Wave")

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Sine Wave Samples at 3Hz")
plt.legend()
plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Define sine wave parameters
frequency = 3  # Hz
amplitude = 1
phase = 0
interval = 0.01  # Sampling interval
samples = 10  # Number of samples
time_samples = np.arange(0, samples * interval, interval)

# Compute sine wave values
sine_wave_values = amplitude * np.sin(2 * np.pi * frequency * time_samples + phase)

# Generate continuous sine wave for comparison
continuous_time = np.linspace(0, samples * interval, 1000)
continuous_sine_wave = amplitude * np.sin(2 * np.pi * frequency * continuous_time + phase)

# Plot samples and continuous sine wave
plt.scatter(time_samples, sine_wave_values, color='red', label="Samples")
plt.plot(time_samples, sine_wave_values, linestyle='dashed', color='blue', label="Interpolated Sine Wave")
plt.plot(continuous_time, continuous_sine_wave, color='green', label="Continuous Sine Wave")

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Sine Wave Samples at 3Hz")
plt.legend()
plt.grid(True)
plt.show()