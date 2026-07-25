import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve
from scipy.fft import fft, ifft

samples, sample_rate = sf.read("Haan Karde.mp3")

# Convert stereo to mono if needed
if len(samples.shape) == 2:
    samples = np.mean(samples, axis=1)

samples = samples.astype(np.float32)

# Normalize
samples = samples / np.max(np.abs(samples))

impulse_responses = {
    "Echo": np.array([1.0, 0.5], dtype=np.float32),

    "Reverb": np.array([1.0, 0.4, 0.2, 0.1], dtype=np.float32),

    "Smooth": np.array([0.2, 0.2, 0.2, 0.2, 0.2], dtype=np.float32)
}

for name, kernel in impulse_responses.items():

    print(f"Processing {name}...")

    # Convolution
    convoluted = convolve(samples, kernel, mode="same")

    convoluted = convoluted / np.max(np.abs(convoluted))


    H = fft(kernel, len(convoluted))

    H[np.abs(H) < 1e-6] = 1e-6

    recovered = np.real(ifft(fft(convoluted) / H))

    recovered = recovered / np.max(np.abs(recovered))

    sf.write(f"{name}_Convolution.wav", convoluted, sample_rate)

    sf.write(f"{name}_Inverse.wav", recovered, sample_rate)


    plt.figure(figsize=(12, 6))

    plt.subplot(3, 1, 1)
    plt.plot(samples)
    plt.title("Original Signal")

    plt.subplot(3, 1, 2)
    plt.plot(convoluted)
    plt.title(f"{name} - Convolved Signal")

    plt.subplot(3, 1, 3)
    plt.plot(recovered)
    plt.title(f"{name} - After Inverse Filtering")

    plt.tight_layout()
    plt.show()

print("Experiment Completed Successfully.")