# Create a variable
running_total = 0

# Create a variable named num_of_friends 
num_of_friends = 4

# Create four variables: appetizers, main_courses, desserts, and drinks.
appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# Use the += operator once to add appetizers, main_courses, desserts, and drinks to running_total.
running_total += appetizers + main_courses + desserts + drinks

# use print() to display the string Total bill so far: followed by a space and the value of running_total
print("Total bill so far:", running_total)

# Create a variable named tip and assign it the result of multiplying running_total by 0.25.
tip = running_total * 0.25
print('Tip amount:', tip) 

# Use the += operator to add the value of tip to your running_total
running_total += tip
print('Total with tip:', running_total)

# Create a variable named final_bill and assign it the result of dividing running_total by num_of_friends
final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

# Use the round() function to round final_bill to two decimal places and assign the result to a new variable named each_pays
each_pays = round(final_bill,2)
print('Each person pays:', each_pays)