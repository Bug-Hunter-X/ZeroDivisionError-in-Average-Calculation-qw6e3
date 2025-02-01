def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list gracefully
    return sum(numbers) / len(numbers) 
    #Could also use statistics.mean(numbers) for a more robust solution