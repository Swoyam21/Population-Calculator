

# Asking User of the seconds between 0 and 86,399
seconds = int(input("Enter number of seconds: "))

# Converting the given seconds into hours.
A_in_hr = seconds // (60 * 60)

# Remaining hours from after deducting A_in_he from seconds
remaining_seconds = seconds - (A_in_hr * 60 * 60)

#converting the remaining seconds into minutes
B_in_min = remaining_seconds // (60)

#converting into seconds.
C_in_seconds = remaining_seconds - (B_in_min * 60)

# Using f-string in print function
print(f"{seconds} seconds is {A_in_hr} hours, {B_in_min} minutes, {C_in_seconds} seconds")






# Total population on January 1, 2022 is 334,205,119.

# Total number of seconds from Jan 1,2022 to jan 20,2022 12:15:20

total_seconds = (19*24*60*60) + (12*60*60) + (15*60) + 20

birth = total_seconds / 7
death = total_seconds / 13
new_imm = total_seconds / 35

# Total population on jan 20, 2022  12:15:20

total_population = round(334205119 + birth - death + new_imm)

print(f"On January 20, 2022 at 12:15:20 the US population was {total_population}")




# Asking user for number of seconds
total_seconds = int(input("Enter seconds since beginning of year: "))

# time in days and Remaining seconds

A_day = total_seconds // (24 * 60 *60)
R_day = total_seconds - (A_day *24 * 60 *60)

# Time in hours and remaining seconds
A_hr = R_day // (60 * 60)
R_hr = R_day - (A_hr * 60 * 60)

# Time in minutes and remaining seconds

A_min = R_hr // (60)

#Remaining seconds
R_min = R_hr - (A_min * 60)






# Calculating birth, death and new immigration.

birth = total_seconds / 7
death = total_seconds / 13
new_imm = total_seconds / 35

# Total population on jan 20, 2022  12:15:20

total_population = int(334205119 + birth - death + new_imm)

print(f"{A_day} days, {A_hr} hours, {A_min} minutes, {R_min} seconds after the start of 2022, the total population was {total_population} .")


# part 4 strats here

F = (((total_population + 350) **2) -12) / 50
F_eaten = round((F)**(1/5))

print(f"The average amount of flapjacks eaten is {F_eaten}")


