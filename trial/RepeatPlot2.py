import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)

for i in range(5):
    # Plot data
    y = np.sin(x + i)
    plt.plot(x, y)

    # Add title and labels
    plt.title(f"Plot {i + 1}")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")

    # Display the current plot
    plt.show()

    # Clear the current figure for the next plot
    plt.clf()
