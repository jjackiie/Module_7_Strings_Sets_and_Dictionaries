# ====================================
# Attached: m7 Class Exercise #7a
# ====================================
# File: Challenge Exercise #1
# ====================================
# Name: Basketball
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this program demonstrates various set operations
baseball = {"jodi", "carmen", "aida", "alicia"}
basketball = {"eva", "carmen", "alicia", "sarah"}

# display members of the baseball set
print("The following students are on the baseball team: ")
for name in baseball:
    print(name)

# display members of the basketball set.
print()
print("The following students are on the basketball team: ")
for name in basketball:
    print(name)

# demonstrate intersection
print()
print("The following students play either basketball or baseball: ")

for name in baseball.union(basketball):
    print(name)

# demonstrate difference of baseball and basketball
print()
print("The following students play basketball, but not baseball: ")
for name in basketball.difference(baseball):
    print(name)

# demonstrate symmetric difference
print()
print("The following students play one sport, but not both: ")
for name in baseball.symmetric_difference(basketball):
    print(name)

''''
=================== Output ===========================
The following students are on the baseball team: 
alicia
carmen
aida
jodi

The following students are on the basketball team: 
eva
sarah
alicia
carmen

The following students play either basketball or baseball: 
jodi
alicia
sarah
aida
eva
carmen

The following students play basketball, but not baseball: 
sarah
eva

The following students play one sport, but not both: 
eva
sarah
jodi
aida

Process finished with exit code 0

'''

# ====================================
# Attached: m7 Class Exercise #7a
# ====================================
# File: Challenge Exercise #2
# ====================================
# Name: Food Items
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# create a GUI with some list boxes items
# import all the tkinder pack
from tkinter import *

# create a Tk root window named top
top = Tk()

# create listbox object
listbox = Listbox(top, height=10, width=15, bg="grey",
                  activestyle="dotbox", font="Arial",
                  fg="yellow", selectmode=MULTIPLE)

# define the size of the window
top.geometry("300x250")

# define the label from the list
label = Label(top, text="FOOD ITEMS")

# insert elements by index with their names as parameters
listbox.insert(1, "Sandwich")
listbox.insert(2, "Burger")
listbox.insert(3, "Pizza")
listbox.insert(4, "French Fries")
listbox.insert(5, "Hot Dogs")
listbox.insert(6, "Cheeseburger")


# function to print the selected value from in the listbox
def selected_item():
    for i in listbox.curselection():
        # traverse the tuple return by curselection method print corresponding value(s) in the listbox
        print(listbox.get(i))


# create a bottom widget and map the command parameter to selected_item function
btn = Button(top, text="Print Selection", command=selected_item)

# placing the bottom in the list box
btn.pack(side="bottom")

# pack the widgets
label.pack()
listbox.pack()

# display until the user exits themselves
top.mainloop()

''''
=================== Output ===========================



'''


# ====================================
# Attached: m7 Class Exercise #7a
# ====================================
# File: Challenge Exercise #3
# ====================================
# Name: The Total Function
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this program will output the numbers list into a text file

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    total = 0

    for value in numbers:
        # total the numbers in the list
        total += value

    # the lens function returns the number of items in the list
    average = total / len(numbers)
    print("The total is ", total, "the average is ", average)

    output = open("numbers.txt", "w")
    output.writelines(str(numbers) + "\n")
    output.writelines(str(total) + "\n")
    output.writelines(str(average) + "\n()")


main()

''''
=================== Output ===========================



'''


# ====================================
# Attached: m7 Class Exercise #7a
# ====================================
# File: Challenge Exercise #4
# ====================================
# Name: Total Sales
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this program will ask for the week sales to get the total and store it in a list

def main():
    days_in_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    week_sales = []

    print("Enter the sales for the week.\n")

    index = 0

    for i in days_in_the_week:
        sale = float(input(f"Enter the sales for {i}: "))
        week_sales.insert(index, sale)
        index += 1

    total_sales = total(week_sales)

    print(f"The total sales of the week is${total_sales:,.2f}")

    write("week_sales.txt", week_sales, total_sales)


def total(numbers):
    sum = 0
    for value in numbers:
        sum += int(value or 0)
    return sum


def write(name, sales, total):
    output = open(name, "w")
    for money in sales:
        output.writelines(str(money) + "\n")
    output.writelines(f"Total sales: ${total:,.2f2}")


''''
=================== Output ===========================



'''


# ====================================
# Attached: m7 Class Exercise #7a
# ====================================
# File: Challenge Exercise #5
# ====================================
# Name: Rainfall
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this program will ask for the monthly rainfall to get the total and store it in a list

def main():
    month_of_the_year = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
    monthly_rain = []

    print("Enter the rainfall for each month.\n")

    index = 0

    for i in month_of_the_year:
        rain = float(input(f"Enter the amount of rain for {i}: "))
        monthly_rain.insert(index, rain)
        index += 1

    total_rain = total(monthly_rain)
    average_rain = total_rain / len(monthly_rain)
    less_rain = min(monthly_rain)
    less_rain_index = monthly_rain.index(less_rain)
    most_rain = max(monthly_rain)
    most_rain_index = monthly_rain.index(most_rain)

    print(f"The total rain in the year was: {total_rain}")
    print(f"The average rain in each month is {average_rain:.2f}")
    print(f"The month with the lowest rain was {month_of_the_year[less_rain_index]} with {less_rain} inches of rain.")
    print(f"The month with the highest rain was {month_of_the_year[most_rain_index]} with {most_rain} inches of rain.")

    write("yearly_rain.txt", monthly_rain, total_rain, month_of_the_year)


def total(numbers):
    sum = 0

    for value in numbers:
        sum += int(value or 0)
    return sum


def write(name, monthly_rain, total_rain, month_of_the_year):
    index = 0

    output = open(name, "w")

    for rain in monthly_rain:
        output.writelines(f"{month_of_the_year[index]}: {rain} inches\n")
        index += 1

    output.writelines(f"Total rain: {total:.2f} inches\n")
    output.writelines(f"The average rain on this year was {total / len(month_of_the_year)} inches\n")

    less_rain = min(monthly_rain)
    less_rain_index = monthly_rain.index(less_rain)
    most_rain = max(monthly_rain)
    most_rain_index = monthly_rain.index(most_rain)

    output.writelines(f"The month with the lowest rain was {month_of_the_year[less_rain_index]} "
                      f"with {less_rain} inches of rain.")
    output.writelines(f"The month with the highest rain was {month_of_the_year[most_rain_index]} "
                      f"with {most_rain} inches of rain.")


main()

''''
=================== Output ===========================



'''
