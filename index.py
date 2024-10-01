# Define the function 
def calculate_discount(price, discount_percent):
   
   if discount_percent >= 20:
      new_price = price - discount_percent*price/100
      return new_price
   else:
      return price
   

# Prompt the user to enter the original price of an item and the discount percentage.
price = int(input("Enter price: "))
discount_percent = int(input("Enter Discount Percent: ")) 

# Calls the function and print the final price after applying the discount, or if no discount was applied, print the original price.
print(calculate_discount(price, discount_percent))