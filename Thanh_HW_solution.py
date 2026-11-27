"""
CSC110 Learning by Crafting: Homework Example Solution
Weekly Spending Tracker
Author: Thanh Luong
"""


def get_total(spending):
    """Return the total of all amounts in the spending list."""
    total = 0
    # Add each day's amount to the running total
    for amount in spending:
        total = total + amount
    return total


def get_average(spending):
    """Return the average amount spent per day."""
    total = get_total(spending)
    average = total / len(spending)
    return average


def find_highest_day(spending):
    """Return the highest amount spent and the day number (1 to 7) it happened."""
    highest = spending[0]
    highest_day = 1
    for i in range(len(spending)):
        if spending[i] > highest:
            highest = spending[i]
            highest_day = i + 1  # index 0 is Day 1, so add 1
    return highest, highest_day


def count_over_budget(spending, budget):
    """Return how many days the amount spent was more than the budget."""
    count = 0
    for amount in spending:
        if amount > budget:
            count = count + 1
    return count


def main():
    """Ask for a daily budget and print a summary of the week's spending."""
    spending = [12.50, 8.00, 23.75, 5.00, 15.25, 30.00, 9.50]

    # Ask the user for a daily budget
    budget = float(input("Enter your daily budget: $"))

    total = get_total(spending)
    average = get_average(spending)
    highest, highest_day = find_highest_day(spending)
    over = count_over_budget(spending, budget)

    # Print the weekly summary
    print("Weekly Spending Summary")
    print("Total spent:", round(total, 2))
    print("Average per day:", round(average, 2))
    print("Highest day: Day", highest_day, "with", highest)
    print("Days over budget:", over)


if __name__ == "__main__":
    main()
