import numpy as np
import matplotlib.pyplot as plt
def unit_impulse(length, period):
    signal = np.zeros(length)
    for i in range(length):
        if(i%period ==0):
            signal[i] = 1
    return signal
# Parameters
start = -10 # Start value of the x-axis range
stop = 10 # Stop value of the x-axis range
step = 1 # Step size
# Generate x-axis values
x = np.arange(start, stop+step, step)
# Generate unit impulse signal
impulse_signal = unit_impulse(len(x), 5)
plt.stem(x, impulse_signal)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Unit Impulse Signal')
plt.grid(True)
plt.show()