import numpy as np
import matplotlib.pyplot as plt
def simulate_continuous_unit_step(time):
    unit_step = np.zeros_like(time)
    unit_step[time >= 0] = 1 
    return unit_step
def simulate_discrete_unit_step(num_samples):
    unit_step = np.zeros(num_samples)
    unit_step[num_samples // 2:] = 1
    return unit_step
# Define the time range for the continuous unit step signal
time = np.linspace(-5, 5, 1000) # Time range from -5 to 5
# Simulate the continuous unit step signal
continuous_unit_step = simulate_continuous_unit_step(time)
# Define the number of samples for the discrete unit step signal
num_samples = 20 # Number of samples
# Simulate the discrete unit step signal
discrete_unit_step = simulate_discrete_unit_step(num_samples)


def simulate_continuous_unit_step(time):
    unit_step = np.zeros_like(time)
    unit_step[time >= 0] = 1
    return unit_step
def simulate_discrete_unit_step(num_samples):
    unit_step = np.zeros(num_samples)
    unit_step[num_samples // 2:] = 1
    return unit_step
# Define the time range for the continuous unit step signal
time = np.linspace(-5, 5, 1000) # Time range from -5 to 5
# Simulate the continuous unit step signal
continuous_unit_step = simulate_continuous_unit_step(time)
# Define the number of samples for the discrete unit step signal
num_samples = 20 # Number of samples
# Simulate the discrete unit step signal
discrete_unit_step = simulate_discrete_unit_step(num_samples)
# Plot and display the continuous and discrete unit step signals
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(time, continuous_unit_step)
plt.title('Continuous Unit Step Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.subplot(2, 1, 2)
plt.stem(discrete_unit_step)
plt.title('Discrete Unit Step Signal')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()
# Save the unit step signal arrays (optional)
# np.savetxt('continuous_unit_step.txt', continuous_unit_step, delimiter=',')
# np.savetxt('discrete_unit_step.txt', discrete_unit_step, delimiter=',')