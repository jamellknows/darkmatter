import matplotlib.pyplot as plt

# Data from [low confidence data begin]
distances = [0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
luminosities = [100000, 50000, 10000, 1000, 100, 10, 1, 0.1, 0.01, 0.001, 0.0001]
# [low confidence data end]



# Plot the data
plt.plot(distances, luminosities)

# Label the axes
plt.xlabel("Distance from the Galactic Center (light-years)")
plt.ylabel("Average Luminosity of Stars (solar luminosities)")

# Title the plot
plt.title("Average Luminosity of Stars vs. Distance from the Galactic Center")

# Show the plot
plt.show()