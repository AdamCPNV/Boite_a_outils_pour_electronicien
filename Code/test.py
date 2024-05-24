def find_closest_combination(target, numbers):
    closest_sum = None
    closest_pair = None

    # Consider multipliers: 1, 10, 100, 1000 (you can extend this as needed)
    multipliers = [1, 10, 100, 1000, 10000, 1000000]

    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            for m1 in multipliers:
                for m2 in multipliers:
                    num1 = numbers[i] * m1
                    num2 = numbers[j] * m2
                    current_sum = num1 + num2
                    if closest_sum is None or abs(current_sum - target) < abs(closest_sum - target):
                        closest_sum = current_sum
                        closest_pair = (num1, num2)

    return closest_pair, closest_sum

# List of numbers
numbers = [1, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]

# Target number
target = float(input("Enter the target number: "))

# Find the closest combination
closest_pair, closest_sum = find_closest_combination(target, numbers)

print(f"The closest combination is: {closest_pair[0]} and {closest_pair[1]}")
print(f"The sum of the closest combination is: {closest_sum}")
print(f"The difference from the target is: {abs(target - closest_sum)}")
