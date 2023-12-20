import random

def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Oops! 😅 Please enter a valid numeric value.")

def get_valid_int(prompt, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if max_value is not None and value > max_value:
                raise ValueError(f"Oops! 😅 Please enter a value less than or equal to {max_value}.")
            return value
        except ValueError:
            print("Oops! 😅 Please enter a valid number.")

def split_paycheck():
    try:
        # Get the user's paycheck amount
        paycheck_amount = get_valid_float("Hey there! 😊 Enter your paycheck amount: $")

        # Find out how many ways the user wants to split it (up to a maximum of 20)
        num_splits = get_valid_int("Nice! 🌟 How many ways would you like to divide it into? (Up to 20) ", max_value=20)

        # Gather the percentages for each split
        percentages = []
        for i in range(num_splits - 1):
            percentage = get_valid_float(f"Awesome! 💰 Enter the percentage for split {chr(65 + i)}: ")
            percentages.append(percentage)

        # Check if the sum of percentages is greater than 100
        total_percentage = sum(percentages)
        while total_percentage > 100:
            print("Oops! 😅 Total percentage exceeds 100%. Please adjust your input.")
            percentages = []
            for i in range(num_splits - 1):
                percentage = get_valid_float(f"Re-enter the percentage for split {chr(65 + i)}: ")
                percentages.append(percentage)
            total_percentage = sum(percentages)

        # Calculate the remaining percentage
        remainder_percentage = 100 - total_percentage
        percentages.append(remainder_percentage)

        # Calculate and display the split amounts
        shares = [paycheck_amount * (percentage / 100) for percentage in percentages]

        print("\nPaycheck Split:")
        for key, value in zip(range(1, num_splits + 1), shares):
            print(f"Split {chr(64 + key)}: ${value:.2f}")

        # Add a random friendly encouraging comment
        encouraging_comments = [
            "Great job! 🚀 You're on the path to hit your financial goals.",
            "Fantastic! 🌈 Your budgeting skills are top-notch.",
            "Keep it up! 🌟 Smart financial decisions lead to success.",
            "You're doing amazing! 🎉 Planning your finances wisely pays off.",
            "Way to go! 🌟 Your commitment to financial planning is admirable.",
            "Impressive! 🌟 Your dedication to financial health is inspiring.",
            "Well done! 🌟 Each step you take brings you closer to financial success.",
            "Outstanding! 🌟 Your financial planning skills keep improving.",
            "Bravo! 🌟 Your wise money management is setting you up for success."
        ]
        print("\n", random.choice(encouraging_comments))

    except Exception as e:
        print(f"Oops! 😅 An unexpected error occurred: {e}")

# Example usage
split_paycheck()
