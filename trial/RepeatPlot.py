import matplotlib.pyplot as plt
import numpy as np
import time

# Example iterative plotting
for i in range(5):
    # Clear the previous plot
    plt.clf()

    # Generate new data
    x = np.linspace(0, 10, 100)
    y = np.sin(x + i)

    # Plot the new data
    plt.plot(x, y)

    # Add some labels
    plt.title(f'Iteration {i}')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')

    # Show the plot (non-blocking)
    plt.pause(1)  # Pause to update the plot with some delay

# Prevent the figure from closing immediately after loop
plt.show()
