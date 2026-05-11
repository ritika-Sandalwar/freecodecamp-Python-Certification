# create a variable to store base price of movie ticket
base_price = 15

# create a variable to store user's age
age = 21

# create a variable to store type of seat the user has selected
seat_type = 'Gold'

# another variable to store show time
show_time = 'Evening'

#  if the user is eligible to book a movie ticket based on their age.
if age > 17:
    print('User is eligible to book a ticket')

#  check whether the user is allowed to book an evening show based on their age.
if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

# create a variable to check whether user is a member 
is_member = False

# another variable to check whether the movie show is on a weekend
is_weekend = False

# variable to store discount the user gets on the ticket
discount = 0

# check if member is truthy and member's age greater than or equal to 21
if is_member and age >= 21 :
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')

# display message that shows updated discount value
print('Discount:', discount)

# another variable that represents extra charges that applied on ticket
extra_charges = 0

# check if is_weekend is truthy or show time is evening
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')

# display updates value of extra charges
print('Extra charges:', extra_charges)

# Users with age 21 or above can always book tickets without any restrictions and Users between 18 and 21 can book tickets, but only when the show_time is not Evening
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member): 
    print('Ticket booking condition satisfied')

    # varible for service charges
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges) # display service charges according to seat type
# calculate the final price of the ticket
    final_price = extra_charges + service_charges + base_price - discount
    print('Final price of ticket:', final_price)
else:
    print('Ticket booking failed due to restrictions')
