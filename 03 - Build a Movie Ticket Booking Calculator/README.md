This workshop contains 21 steps 👣
-------------------------------------------------------------------------------------------------------
▫ Step 1 : Create a variable named base_price to store the base price of the movie ticket and set its value to 15. Create another variable named age to store the user's age and set its value to 21.

▫ Step 2 : Create a variable named seat_type to store the type of seat the user has selected and set its value to the string Gold. Create another variable named show_time to store the show time of the movie and set its value to the string Evening.

▫ Step 3 : Create an if statement to check if age is greater than 17. Inside the body of the if statement, print User is eligible to book a ticket.

▫ Step 4 : Create an if statement to check if age is greater than or equal to 21. Inside the body of the if statement, print User is eligible for Evening shows.

▫ Step 5 : Now, add an else clause to your if statement and print User is not eligible for Evening shows inside the else body.

▫ Step 6 : Create a variable named is_member to indicate whether the user is a member and set its value to True. Below the is_member variable create another variable named is_weekend to indicate whether the movie show is on a weekend and sets its value to False.

▫ Step 7 : Create a variable named discount and set its value to 0. This will store the discount the user gets on the movie ticket.

▫ Step 8 : Create an if statement to check if is_member is truthy. Inside the body of the if statement, update the discount value to 3 and print User qualifies for membership discount to the terminal.

▫ Step 9 : Add an else clause to your if statement and print User does not qualify for membership discount inside the else body. You also want to display the updated value of discount. Below the if...else statement, use the print() call to display a message that shows Discount: followed by the updated value of discount.

▫ Step 10 : Update the condition of the if is_member: line by using the and operator to combine the existing condition with another condition checking if age is greater than or equal to 21. (The membership discount should only apply to members if their age is greater than or equal to 21).

▫ Step 11 : Now change the value of the is_member variable to False as the user is not a member. After that, you will see that the discount value now remains 0, because both conditions must be satisfied for the discount to apply.

▫ Step 12 :  Create a variable named extra_charges and set it to 0. (represent extra charges to apply to the movie ticket on weekends). Create an if statement to check if is_weekend is truthy. Inside the body of if statement, update the extra_charges value to 2 and print Extra charges will be applied in the terminal.

▫ Step 13 : Add an else clause to your if statement and print No extra charges will be applied inside the else body. Below the else clause, use the print() call to display a message that shows Extra charges: followed by the updated value of extra_charges and check the output in the terminal.

▫ Step 14 : Extra charges should also apply if the show is in the evening. Update the condition of the if is_weekend: line by using the or operator to combine the existing condition with a second condition checking if show_time is equal to the string Evening.

▫ Ste;p 15 : Create an if statement to check if age is greater than or equal to 21. Inside the body of the if statement, print Ticket booking condition satisfied to the terminal. Then, add an else clause to your if statement and print Ticket booking failed due to restrictions inside the else body.

▫ Step 16 : Update the condition of the if age >= 21: line. Use the and operator to build an expression checking if age is greater than or equal to 18 and show_time is not Evening. Then use the or operator to combine that expression with the existing condition. (Users between 18 and 21 can book tickets, but only when the show_time is not Evening).

▫ Step 17  : Update the condition of the if age >= 21 or age >= 18 and show_time != 'Evening': line to add another condition using the or operator to check if is_member is truthy. Use parentheses () to group the show_time != 'Evening' and is_member conditions together.

▫ Step 18 : Inside the body of the last if statement, below the print('Ticket booking condition satisfied') line, create a variable named service_charges and set it to 0. Then, create a nested if statement to check if seat_type is equal to Premium. Inside the body of the nested if statement, update the service_charges value to 5.

▫ Step 19 : Still inside the body of the outer if statement, add an else clause to the nested if seat_type == 'Premium': statement and update the service_charges value to 1 inside the else body.

▫ Step 20 : Still inside the body of the outer if statement, add an elif clause between the if seat_type == 'Premium': and else: lines and check if seat_type is equal to Gold. Inside the body of the elif clause, update the value of service_charges to 3. Below the nested if...elif...else statement, use the print() call to display a message that shows Service charges: followed by the updated value of service_charges.

▫ Step 21 : Inside the body of the last if statement, below the print('Service charges:', service_charges) line, calculate the final price of the ticket and store it in a variable named final_price. (The final ticket price is calculated by adding the extra charges and service charges to the base price, and then subtracting the discount). Finally, print a message that shows Final price of ticket: followed by the value of final_price.

And this is the Final Output :

  <img width="490" height="190" alt="Screenshot (261)" src="https://github.com/user-attachments/assets/247e6503-4c7e-45f4-8021-0bad69447631" />
