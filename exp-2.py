import numpy as np
import matplotlib.pylab as plt

def liner_convolution(signal1, signal2):
    linear_conv = np.convolve(signal1,signal2, mode='full')
    return linear_conv

def circular_convolution(signal1, signal2):
    fft_length = max(len(signal1),len(signal2))
    fft_signal1 = np.fft.fft(signal1,fft_length)
    fft_signal2 = np.fft.fft(signal2,fft_length)
    circular_convo = np.fft.ifft()