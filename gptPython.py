import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_random_data(seed=0, size=(100, 2)):
    """Generate random data with a given seed."""
    np.random.seed(seed)
    return np.random.randn(*size)

def plot_descriptive_statistics(ax, data):
    """Plot bar charts for mean and median of each variable."""
    variables = [data[:, 0], data[:, 1]]
    labels = ['Variable 1', 'Variable 2']
    colors = ['blue', 'green']

    for i, (variable, label, color) in enumerate(zip(variables, labels, colors)):
        ax.bar(['Mean', 'Median'], [np.mean(variable), np.median(variable)], color=color, alpha=0.7, label=label)

    ax.legend()
    ax.set_title('Descriptive Statistics: Mean and Median')

def plot_correlation_analysis(ax, data):
    """Plot a heatmap for correlation analysis."""
    sns.heatmap(np.corrcoef(data.T), annot=True, ax=ax)
    ax.set_title('Correlation Analysis')

def plot_histogram(ax, data):
    """Plot histograms for each variable."""
    colors = ['blue', 'green']
    labels = ['Variable 1', 'Variable 2']

    for variable, color, label in zip(data.T, colors, labels):
        ax.hist(variable, bins=15, color=color, alpha=0.7, label=label)

    ax.legend()
    ax.set_title('Histogram of Variables')

def plot_scatter(ax, data):
    """Plot a scatter plot of Variable 1 vs Variable 2."""
    ax.scatter(data[:, 0], data[:, 1], alpha=0.7)
    ax.set_xlabel('Variable 1')
    ax.set_ylabel('Variable 2')
    ax.set_title('Scatter Plot of Variable 1 vs Variable 2')

def main():
    # Generate random data
    data = generate_random_data(seed=0, size=(100, 2))

    # Create a 2x2 subplot
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Call modular functions to plot different parts of the analysis
    plot_descriptive_statistics(axes[0, 0], data)
    plot_correlation_analysis(axes[0, 1], data)
    plot_histogram(axes[1, 0], data)
    plot_scatter(axes[1, 1], data)

    # Adjust layout and display the plot
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

