#!/usr/bin/python3
# Problem : Receive and convert to kilometers
# kilometers = miles * 1.60934
# 5 miles aquals 8.04 kilometers

# Ask the user miles and assign it to the miles variable
miles = input("Enter Miles")

# Convert from string to integer
miles = int(miles)

# Perform calculation by multiplying 1.60934 times miles
kilometers = miles * 1.60934

# Print results using format()
print("{} miles equals {} kilometers".format(miles, kilometers))