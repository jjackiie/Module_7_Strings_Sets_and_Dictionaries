# ====================================
# Attached: m7 Class Exercise #7a
# ====================================
# File: Project #1
# ====================================
# Name:
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this program demonstrates several strings testing methods.

def main():
    # get a string from the user
    user_string = input("Enter a string: ")

    print("This is what I found about that string:")

    # test the string
    if user_string.isalnum():
        print("The string is alphanumeric.")
    if user_string.isdigit():
        print("The string contains only digits.")
    if user_string.isalpha():
        print("The string contains only alphabetic characters.")
    if user_string.isspace():
        print("The string contains only whitespace characters.")
    if user_string.islower():
        print("The letters in the string are all lowercase.")
    if user_string.isupper():
        print("The letters in the string are all uppercase.")


# call the string
main()



''''
=================== Output ===========================


'''


# ====================================
# Attached: m7 Class Exercise #7a
# ====================================
# File: Project #2
# ====================================
# Name:
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# the get_login_name function accepts a first name,
# last name and ID number as arguments. It returns a system login name.

def get_login_name(first, last, idnumber):
    # get the first three letter of the first name. if the name is less than 3 characters,
    # the slice will return the entire first name.
    set1 = first[0: 3]
    set2 = last[0: 3]
    set3 = idnumber[0: 3]

# get the first three letters of the last name.


''''
=================== Output ===========================


'''