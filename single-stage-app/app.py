import matplotlib.pyplot as plt
import numpy as np
import os

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a simple plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2)
plt.title('Sine Wave', fontsize=16)
plt.xlabel('X axis', fontsize=14)
plt.ylabel('Y axis', fontsize=14)
plt.grid(True)

# Make sure output directory exists
os.makedirs('output', exist_ok=True)

# Save the figure
plt.savefig('output/sine_wave.png')
print("Graph generated and saved to output/sine_wave.png")

