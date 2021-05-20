# Leap Year program
# Khai Phan
# 933-290-231
# CS 362 Spring Term 2021

# Determine if year entered is a leap year
# Year entered must be integer (assumed to be integer input)
def is_leapyear(year):

    # Check if divisible by 4
    if year % 4 == 0:

        # Check if divisible by 100
        if year % 100 == 0:

            # Check if divisible by 400
            if year % 400 == 0:

                # It is a leap year
                # print(f"{year} is a leap year.")
                return True

            else:

                # It is not a leap year
                # print(f"{year} is NOT a leap year.")
                return False

        else:

            # It is a leap year
            # print(f"{year} is a leap year.")
            return True

    else:

        # It is not a leap year
        # print(f"{year} is NOT a leap year.")
        return False
