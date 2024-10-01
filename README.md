# Discount Calculation Program
This Python script calculates the discounted price of an item based on the original price and discount percentage provided by the user. If the discount is 20% or more, it applies the discount and returns the new price. Otherwise, it returns the original price without any discount applied.

## How It Works
1. Define a function:
The script defines a function called calculate_discount that:

- Takes two arguments: price (original price of the item) and discount_percent (percentage discount).
- If the discount is greater than or equal to 20%, it applies the discount and returns the new price.
- If the discount is less than 20%, it returns the original price without any discount.

2. Get user input:
The program prompts the user to input:

- The original price of the item.
- The discount percentage.

3. Call the function and print the result:
The script calls the calculate_discount function with the user's inputs and prints the resulting price (whether discounted or not).

## Requirements
Python 3.x installed on your system.
## How to Run
1. Download or copy the script to your local machine.
2. Open a terminal or command prompt and navigate to the directory where the script is saved.
3. Run the script by typing:
    <code>python <script_name>.py</code>
4. Enter the price and discount percentage when prompted.
## Notes
Ensure that the price and discount_percent values entered are positive integers.
The function only applies the discount if it is 20% or higher. Otherwise, the original price is returned unchanged.
The calculation for the discount is based on the percentage provided by the user, so make sure to enter accurate values.