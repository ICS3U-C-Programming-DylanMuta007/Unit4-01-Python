#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date : March 2025
# Calculates the sum up until the provided number by the user (limited to 100)


def main():
    # Get user_numb as string
    user_numb_as_string = input("Input a positive integer: ")

    try:
        # Tries to convert the string into an integer
        user_numb_as_int = int(user_numb_as_string)

        # Checks if the user input is less than 0 or more than 100
        if user_numb_as_int < 0 or user_numb_as_int > 100:
            print("\nPlease chose a positive integer or a number less than 100")

        else:
            # Sets counter and sum to 0
            counter = 0
            sum = 0

            # Loops until the counter is the same as user_numb_as_int
            while counter < user_numb_as_int:
                counter = counter + 1
                sum = sum + counter
                print(f"Tracking {counter} times through the loop")
            # Shows the sum from 0 to user input
            print(f"\nthe sum from 0 to {user_numb_as_int} = {sum}")

    # If the user_input cant be converted prints the catch statement
    except ValueError:
        print("\nPlease input a number")


if __name__ == "__main__":

    main()
