# bill_splitter.py

def split_bill(total_amount, num_people, tip_percentage=0):
    """Calculates how much each person should pay, including tip."""
    
    if num_people <= 0:
        return "Number of people must be greater than zero!"
    
    tip_amount = (total_amount * tip_percentage) / 100
    final_amount = total_amount + tip_amount
    per_person_amount = final_amount / num_people

    print(f"\nTotal Bill: ${total_amount:.2f}")
    print(f"Tip ({tip_percentage}%): ${tip_amount:.2f}")
    print(f"Final Amount (with tip): ${final_amount:.2f}")
    print(f"Each person should pay: ${per_person_amount:.2f}")

# Get user input
total_amount = float(input("Enter the total bill amount: $"))
num_people = int(input("Enter the number of people to split the bill: "))
tip_percentage = float(input("Enter tip percentage (optional, default is 0): "))

# Calculate bill split
split_bill(total_amount, num_people, tip_percentage)
