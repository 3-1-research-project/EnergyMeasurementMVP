import numpy as np
import scipy.stats as stats


def analyze_energy_data(energy_measurements, confidence=0.95):
    n = len(energy_measurements)
    mean_energy = np.mean(energy_measurements)
    std_dev = np.std(energy_measurements, ddof=1)  # Sample standard deviation
    sem = std_dev / np.sqrt(n)  # Standard error of the mean

    # t-score for the given confidence level and degrees of freedom (n-1)
    t_score = stats.t.ppf((1 + confidence) / 2, df=n - 1)

    # Confidence Interval
    margin_of_error = t_score * sem
    confidence_interval = (mean_energy - margin_of_error, mean_energy + margin_of_error)

    # Print results
    print(f"Mean Energy Consumption: {mean_energy:.2f} J")
    print(f"Standard Deviation: {std_dev:.2f} J")
    print(f"Standard Error of the Mean (SEM): {sem:.2f} J")
    print(f"{confidence*100:.0f}% Confidence Interval: {confidence_interval}")

    return mean_energy, std_dev, sem, confidence_interval


def calculate_required_sample_size(std_dev, margin_of_error, confidence=0.95):
    z_score = stats.norm.ppf((1 + confidence) / 2)  # Z-score for normal distribution
    required_n = (z_score * std_dev / margin_of_error) ** 2
    return int(np.ceil(required_n))  # Round up to ensure enough samples


# Example usage:
energy_measurements = [
    635.8,
    641.3,
]  # Replace with your own values

confidence_percentage = 0.95

analyze_energy_data(energy_measurements, confidence_percentage)

# Example for required sample size calculation:
estimated_std_dev = np.std(energy_measurements, ddof=1)
margin_of_error =  1 # Set your desired precision in Joules
required_n = calculate_required_sample_size(estimated_std_dev, margin_of_error, confidence_percentage)
print(f"Required Sample Size for {margin_of_error}J margin of error: {required_n}")
