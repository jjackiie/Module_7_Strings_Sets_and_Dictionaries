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

    # get the first three letters of the last name. if the name is less than 3 characters,
    # the slice will return the entire last name.
    set2 = last[0: 3]

    # get the last three characters of the student ID. if the ID number is less than 3 characters,
    # the slice will return the entire ID number.
    set3 = idnumber[-3:]

    # put the sets of characters together
    login_name = set1 + set2 + set3

    # return the login name
    return login_name


# the valid_password function accepts a password as
# an argument and returns either true or false to
# indicate whether the password is valid. a vaild
# password must be at least 7 characters in length,
# have at least one uppercase letter, one lowercase
# letter, and one digit.

def valid_password(password):
    # set the boolean variables to false
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    # begin the validation. start by testing the password's length.
    if len(password) >= 7:
        correct_length = True

        # test each character and set the
        # appropriate flag when a required
        # character is found.
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True

    # determine whether all the requirements
    # are met. if they are, set is_valid to true.
    # otherwise, set is_valid to false.
    if correct_length and has_uppercase and \
            has_lowercase and has_digit:
        is_valid = True
    else:
        is_valid = False

    # return the is_valid variable.
    return is_valid


# this program gets a password from the user
# and validates it.

import login


def main():
    # get a password from the user.
    password = input("Enter your password: ")

    # validate the password
    while not login.valid_password(password):
        print("That password is not valid.")
        password = input("Enter your password: ")

    print("That is a valid password.")


main()

''''
=================== Output ===========================


'''
