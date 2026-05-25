import math

def mean(data):
    """Return the average of a list of numbers."""
    if len(data) == 0:
        return None
    
    total = sum(data)
    return total / len(data)


def median(data):
    """Return the median (middle value) of a list of numbers."""
    if len(data) == 0:
        return None
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:
        # Even number of values → average of two middle numbers
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        # Odd number of values → middle value
        return sorted_data[mid]


def mode(data):
    """Return the most frequent value(s) in a list."""
    if len(data) == 0:
        return None
    
    frequency = {}
    
    for value in data:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1

    max_count = max(frequency.values())

    modes = []
    for key, count in frequency.items():
        if count == max_count:
            modes.append(key)

    return modes


def data_range(data):
    """Return the range (max - min) of a list of numbers."""
    if len(data) == 0:
        return None
    
    return max(data) - min(data)


def standard_deviation(data):
    """Return the standard deviation of a list of numbers."""
    if len(data) == 0:
        return None
    
    avg = mean(data)
    
    squared_diffs = []
    for value in data:
        diff = value - avg
        squared_diffs.append(diff ** 2)

    variance = sum(squared_diffs) / len(data)
    return math.sqrt(variance)


def frequency_distribution(data):
    """Return a dictionary counting how often each value appears."""
    frequency = {}
    
    for value in data:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1

    return frequency