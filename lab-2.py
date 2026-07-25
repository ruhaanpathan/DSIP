<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt


def linear_convolution(signal1, signal2):
    return np.convolve(signal1, signal2, mode='full')


def circular_convolution(signal1, signal2):
    fft_length = max(len(signal1), len(signal2))

    fft_signal1 = np.fft.fft(signal1, fft_length)
    fft_signal2 = np.fft.fft(signal2, fft_length)

    circular_conv = np.fft.ifft(fft_signal1 * fft_signal2)

    return np.real(circular_conv)

signal1 = np.array([1, 2, 3, 4, 5])
signal2 = np.array([2, 4, 6, 8, 10])


linear_conv = linear_convolution(signal1, signal2)

circular_conv = circular_convolution(signal1, signal2)


print("Signal 1 :", signal1)
print("Signal 2 :", signal2)

print("\nLinear Convolution")
print(linear_conv)

print("\nCircular Convolution")
print(circular_conv)


plt.figure(figsize=(10,6))

plt.subplot(2,1,1)
plt.stem(linear_conv)
plt.title("Linear Convolution")
plt.xlabel("Sample")
plt.ylabel("Amplitude")

plt.subplot(2,1,2)
plt.stem(circular_conv)
plt.title("Circular Convolution")
plt.xlabel("Sample")
plt.ylabel("Amplitude")

plt.tight_layout()
=======
import numpy as np
import matplotlib.pyplot as plt


def linear_convolution(signal1, signal2):
    return np.convolve(signal1, signal2, mode='full')


def circular_convolution(signal1, signal2):
    fft_length = max(len(signal1), len(signal2))

    fft_signal1 = np.fft.fft(signal1, fft_length)
    fft_signal2 = np.fft.fft(signal2, fft_length)

    circular_conv = np.fft.ifft(fft_signal1 * fft_signal2)

    return np.real(circular_conv)

signal1 = np.array([1, 2, 3, 4, 5])
signal2 = np.array([2, 4, 6, 8, 10])


linear_conv = linear_convolution(signal1, signal2)

circular_conv = circular_convolution(signal1, signal2)


print("Signal 1 :", signal1)
print("Signal 2 :", signal2)

print("\nLinear Convolution")
print(linear_conv)

print("\nCircular Convolution")
print(circular_conv)


plt.figure(figsize=(10,6))

plt.subplot(2,1,1)
plt.stem(linear_conv)
plt.title("Linear Convolution")
plt.xlabel("Sample")
plt.ylabel("Amplitude")

plt.subplot(2,1,2)
plt.stem(circular_conv)
plt.title("Circular Convolution")
plt.xlabel("Sample")
plt.ylabel("Amplitude")

plt.tight_layout()
>>>>>>> 07732a736f45a00ecfb96693568c5fabc0c096f4
plt.show()