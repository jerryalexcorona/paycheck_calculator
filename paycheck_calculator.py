def split_paycheck(amount, num_splits, percentages):
    if not isinstance(amount, (int, float)):
        return "Please enter a valid numeric paycheck amount."

    if not isinstance(num_splits, int) or num_splits <= 0:
        return "Please enter a valid positive integer for the number of splits."

    if not all(isinstance(percentage, (int, float)) and 0 <= percentage <= 100 for percentage in percentages):
        return "Please enter valid percentages between 0 and 100."

    total_percentage = sum(percentages)
    if total_percentage > 100:
        return "Total percentage exceeds 100%. Please adjust your input."

    remainder_percentage = 100 - total_percentage
    percentages.append(remainder_percentage)
    
    shares = [amount * (percentage / 100) for percentage in percentages]

    result = dict(zip(range(1, num_splits + 1), shares))
    return result

# Example usage:
paycheck_amount = float(input("Enter your paycheck amount: "))
num_splits = int(input("How many ways would you like to divide it into? "))
percentages = []

for i in range(num_splits - 1):
    percentage = float(input(f"What percentage goes into split {chr(65 + i)}? "))
    percentages.append(percentage)

result = split_paycheck(paycheck_amount, num_splits, percentages)
print("\nPaycheck Split:")
for key, value in result.items():
    print(f"Split {chr(64 + key)}: ${value:.2f}")
