print("This program computes the Greatest Common Factor (GCF) of how ever many integers of your choosing.\n")

number_list = [] #initializes list of numbers to compute the GCF of
list_of_factors = [] #initializes list of factors for each number above
common_factors = [] #initializes list of shared factors from factors above

try: #in case someone inputs zero or a non-integer
    total_numbers = int(input("How many numbers would you care to compute the GCF of?  "))

    for k in range(1, total_numbers + 1):
        number_k = int(input("Please input number " + str(k) + " of " + str(total_numbers) + ":  "))
        number_list.append(number_k) #takes numbers from user one at a time

    for number in number_list: #gathers factors from each number the user inputted
        for i in range(1, number + 1):
            if number % i == 0:
                list_of_factors.append(i)

    for factor in list_of_factors: #tests for shared/common factors between user's inputted numbers
        if list_of_factors.count(factor) == total_numbers:
            common_factors.append(factor)

    print(max(common_factors)) #greatest common factor

except ValueError: #in case a zero, string or float was entered.
    print("Only positive integers can be entered in this program!  Please try again.")