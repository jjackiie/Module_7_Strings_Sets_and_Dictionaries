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


# ====================================
# Attached: m7 Class Exercise #7a
# ====================================
# File: Project #3
# ====================================
# Name:
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this program demonstrates how to tokenize strings.

def main():
    # strings to tokenize
    str1 = "one two three four"
    str2 = "10:20:30:40:50"
    str3 = "a/b/c/d/e/f"

    # display the tokens in each string
    display_tokens(str1, " ")
    print()
    display_tokens(str2, ":")
    print()
    display_tokens(str3, "/")


# the display_tokens function displays the tokens
# in a string, the data parameter is the string to
# tokenize and the delimiter parameter is the delimiter.
def display_tokens(data, delimiter):
    tokens = data.split(delimiter)
    for item in tokens:
        print(f"Token: {item}")


# execute the main function
main()

''''
=================== Output ===========================


'''


# ====================================
# Attached: m7 Class Exercise #7a
# ====================================
# File: Project #4
# ====================================
# Name:
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this program reads test scores from a CSV file
# and calculates each student's test average.

def main():
    # open the file
    csv_file = open("test_scores.csv", "r")

    # read the file's lines into a list
    lines = csv_file.readlines()

    # close the file
    csv_file.close()

    # process the lines
    for line in lines:
        # get the test scores as tokens
        tokens = line.split(",")

        # calculate the total of the test scores
        total = 0.0
        for token in tokens:
            total += float(token)

        # calculate the average of the test scores
        average = total / len(tokens)
        print(f"Average: {average}")


# execute the main function
main()

''''
=================== Output ===========================


'''


# ====================================
# Attached: m7 Class Exercise #7a
# ====================================
# File: Project #5
# ====================================
# Name:
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this program counts the number of times
# the letter T (uppercase or lowercase)
# appears in a string

def main():
    # create a variable to use to hold the count.
    # the variable must start with 0
    count = 0

    # get a string from the user
    my_string = input("Enter a sentence: ")

    # count the Ts
    for ch in my_string:
        if ch == "T" or ch == "t":
            count += 1

    # print the results
    print(f"The letter T appears {count} times.")


# call the main function
main()

''''
=================== Output ===========================


'''
