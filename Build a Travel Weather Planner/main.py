# create a variable distance_mi (a number representing the distance to travel in miles)
distance_mi = 5

# create a variable is_raining (a boolean representing if the user is currently experiencing rainy weather)
is_raining = True

# create a variable has_bike (a boolean representing if the user has a bicycle)
has_bike = True

# create a variable has_car (a boolean representing if the user has a car)
has_car = False

# create a variable has_ride_share_app (a boolean representing if the user has an app that allows them to request a ride)
has_ride_share_app = False

# If distance_mi is a falsy value: You should print False. If the distance is less than or equal to 1 mile: You should print True only if it is not raining.
if distance_mi and distance_mi <= 1 and not is_raining :
    print('True')

# If the distance is greater than 1 mile and less than or equal to 6 miles: You should print True only if the person has a bike and it is not raining.
elif distance_mi > 1 and distance_mi <= 6 and has_bike and not is_raining :
    print('True')

# If the distance is greater than 6 miles: You should print True if the person has a car or has a ride-share app.    
elif distance_mi > 6 and (has_car or has_ride_share_app):
    print('True')  

# Otherwise false
else:
    print('False')

