def two_sum(nums, target):
    # Create a dictionary to store the numbers and their indices
    num_map = {}
    # Iterate through the list of numbers
    for index, num in enumerate(nums):
        # Calculate the complement number needed to reach the target
        complement = target - num
        # Check if the complement is already in the map
        if complement in num_map:
            return [num_map[complement], index]
        # Store the current number and its index in the map
        num_map[num] = index
    # If no solution is found, return an empty list
    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print("Indices:", result)
