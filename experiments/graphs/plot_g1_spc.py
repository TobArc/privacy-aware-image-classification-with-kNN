import matplotlib.pyplot as plt

# Sample-per-class accuracy data for STL-10
stl10_accuracy = {'1': 0.521, '2': 0.552, '4': 0.638, '8': 0.788, '16': 0.891, '32': 0.951, '64': 0.975, '128': 0.985, '256': 0.992, '512': 0.995}

# Sample-per-class accuracy data for CIFAR-10 (replace with actual data)
cifar10_accuracy = {'1': 0.742, '2': 0.764, '4': 0.774, '8': 0.877, '16': 0.947, '32': 0.972, '64': 0.98, '128': 0.983, '256': 0.987, '512': 0.989}

# Convert the keys (samples per class) to integers and sort them
samples_stl10 = sorted([int(k) for k in stl10_accuracy.keys()])
accuracy_stl10 = [stl10_accuracy[str(k)] * 100 for k in samples_stl10]  # Convert to percentage

samples_cifar10 = sorted([int(k) for k in cifar10_accuracy.keys()])
accuracy_cifar10 = [cifar10_accuracy[str(k)] * 100 for k in samples_cifar10]  # Convert to percentage

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(samples_stl10, accuracy_stl10, marker='o', label='STL-10', color='blue')
plt.plot(samples_cifar10, accuracy_cifar10, marker='o', label='CIFAR-10', color='red')

# Adding title and labels
plt.title('Sample-per-Class Accuracy Comparison')
plt.xlabel('Number of Samples per Class')
plt.ylabel('Accuracy (%)')
plt.xscale('log')  # Use a logarithmic scale for the x-axis
plt.ylim(50, 100)  # Set y-axis limits to 0-100 for percentage
plt.xticks(samples_stl10, samples_stl10)  # Ensure X-ticks are the sample numbers
plt.grid(True)

# Adding a legend
plt.legend()

# Show the plot
plt.show()