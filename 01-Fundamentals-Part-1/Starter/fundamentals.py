# ## Print - One of the simplest (and most important!) tasks you can ask a computer to do is to print a message. The code is inside the box (known as a code cell), and the computer's response (called the output of the code) is shown below the box. 

# print("Hello, world!")
# print (["Yuri", 100, 25.20])


# ## Arithmetic


# print(2 + 1)
# print(2 - 1)
# print(9 - 5)
# print(2 * 2) # Multiply 2 by 2
# print(4 / 2)
# print(2 ** 3)
# print(((1+3) * (9 - 2) / 2) ** 2)

# ## Variables - So far, you have used code to make a calculation and print the result, and the result isn't saved anywhere. However, you can imagine that you might want to save the result to work with it later. For this, you'll need to use variables.

# # Create a variable called test_var and give it a value of 4+5
# test_var = 4 + 5
# # Print the value of test_var
# print(test_var)

# # Nao pode ter espacos, apenas incluir letras, mumeros e _, iniciar apenas com letras ou _, test_var! and 1_var is not allowed

# my_var = 3
# print(my_var)
# my_var = 100 # Chabge the value assigned to my_var
# print(my_var)
# print(type(my_var))

# # Increase the value by 3
# my_var = my_var + 3
# print(my_var)


# a = 5
# b = 1.1
# print(a)
# print(a+b)
# print(type(a))
# print(type(b))

# # Using Multiple Variables
# num_years = 4
# days_per_year = 365
# hours_per_day = 24
# mins_per_hour = 60
# secs_per_min = 60

# # Calculate the number of seconds in four years

# total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
# print(total_secs)

# # Update to include leap years - devemos escrever a equacao novamente apos atualizar a variavel days_per_year
# days_per_year = 365.25
# total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
# print(total_secs)

# my_income = 1000 # salario
# tax_rate = 0.15 # 15% de impostos 
# may_taxes = my_income * tax_rate
# print(may_taxes)


# ## Functions - A function is a block of code designed to perform a specific task. 


# # Define the function
# def add_three(input_var): # header
#     output_var = input_var + 3 # body
#     return output_var

# # Run or call a function
# new_number = add_three(10)
# print(new_number)


# def get_pay(num_hours):
#     pay_pretax = num_hours * 15
#     pay_aftertax = pay_pretax * (1 - .12)
#     return pay_aftertax

# pay_fulltime = get_pay(40)
# print(pay_fulltime)

# pay_fulltime = get_pay(32)
# print(pay_fulltime)

# # Functions with multiple arguments
# # , = comma
# # : = colon 

# def get_pay_with_more_inputs (num_hours, hourly_wage, tax_bracket):
#     pay_pretax = num_hours * hourly_wage
#     pay_aftertax = pay_pretax * (1 - tax_bracket)
#     return pay_aftertax

# salary_aftertax = get_pay_with_more_inputs(40, 24, .22)
# print(salary_aftertax)

# salary_aftertax = get_pay_with_more_inputs(40, 15, .12)
# print(salary_aftertax)

# # Functions with no arguments

# def message_general():
#     print("Hello, you!")
#     print("Good morning!")

# message_general()


# ## Data Types - integers, floats, booleans, and strings.

# ## Integers
# # positive and negative numbers without any fractional part (0, 1, 2, 3, ...)

# x = 14
# print(x)
# print(type(x))

# # Floats
# # Floats are numbers with fractional parts. They can have many numbers after decimal.

# nearly_pi = 3.141592653589793238462643383279502
# print(nearly_pi)
# print(type(nearly_pi))

# # We can also specify a float with a fraction.
# almost_pi = 22/7
# print(almost_pi)
# print(type(almost_pi))

# # One function that is particularly useful for fractions is the round() function. It lets you round a number to a specified number of decimal places.
# # Round to 5 decimal places
# rounded_pi = round(almost_pi, 5)
# print(rounded_pi)
# print(type(rounded_pi))

# rounded_pi = round(almost_pi, 0)
# print(rounded_pi)
# print(type(rounded_pi))

# # Whenever you write an number with a decimal point (.), Python recognizes it as a float data type.
# y_float = 1.
# print(y_float)
# print(type(y_float)) #float

# y_float = 1
# print(y_float)
# print(type(y_float)) #int


# ## Booleans - represent one of two values: True or False. In the code cell below, z_one is set to a boolean with value True
# from pickle import FALSE


# z_one = True
# print(z_one)
# print(type(z_one))

# z_two = False
# print(z_two)
# print(type(z_two))

# # Booleans are used to represent the truth value of an expression. Since 1 < 2 is a true statement, z_three takes on a value of True.
# z_three = (1 < 2) #True
# print(z_three)
# print(type(z_three))

# z_four = (5 < 3)
# print(z_four)
# print(type(z_four)) #False

# # We can switch the value of a boolean by using (not). So, not True is equivalent to False, and not False becomes True.

# z_five = not z_four
# print(z_five)
# print(type(z_five)) #True


# ## Strings - The string data type is a collection of characters (like alphabet letters, punctuation, numerical digits, or symbols) contained in quotation marks. Strings are commonly used to represent text.

# w = "Hello, Python!"
# print(w)
# print(type(w))
# print(len(w))

# # One special type of string is the empty string, which has length zero.
# shortest_string = ""
# print(type(shortest_string))
# print(len(shortest_string))

# # Converting numbers in string

# my_number = "1.12321"
# print(my_number)
# print(type(my_number))

# # If we have a string that is convertible to a float, we can use float().

# also_my_number = float(my_number)
# print(also_my_number)
# print(type(also_my_number))

# # ust like you can add two numbers (floats or integers), you can also add two strings. It results in a longer string that combines the two original strings by concatenating them.

# new_string = "abc" + "def"
# print(new_string)
# print(type(new_string))

# # Note that it's not possible to do subtraction or division with two strings. You also can't multiply two strings, but you can multiply a string by an integer. This again results in a string that's just the original string concatenated with itself a specified number of times.

# newest_string = "abc" * 3
# print(newest_string)
# print(type(newest_string))

# # Note that you cannot multiply a string by a float! Trying to do so will return an error.

# # will_not_work = "abc" * 3.


# ## CONDITIONS- In programming, conditions are statements that are either True or False.


# print(2 > 3)

# # You can also use conditions to compare the values of variables. 
# var_one = 1
# var_two = 2

# print (var_one < 1)
# print (var_two >= var_one)

#  #   Symbol	Meaning
#  #   ==	equals
#  #   !=	does not equal
#  #   <	less than
#  #   <=	less than or equal to
#  #   >	greater than
#  #   >=	greater than or equal to

#  # Important Note: When you check two values are equal, make sure you use the == sign, and not the = sign.

#  # Conditional statements
#  # "if" statements

# def evaluate_temp(temp):
#     message = "Normal temperature"
#     if temp > 38:
#         message = "Fever!"
#     return message

# print(evaluate_temp(37))

# print(evaluate_temp(39))
 
# # "if ... else" statements - We can use "else" statements to run code if a statement is False. The code under the "if" statement is run if the statement is True, and the code under "else" is run if the statement is False.

# def evaluate_temp_while_else(temp):
#     if temp > 38:
#         message = "Fever!"
#     else:
#         message = "Normal temperature"
#     return message

# print(evaluate_temp_while_else(37))

# # "if ... elif ... else" statements - We can use "elif" (which is short for "else if") to check if multiple conditions might be true

# def evaluate_temp_with_elif(temp):
#     if temp > 38:
#         message = "Fever!"
#     elif temp > 35:
#         message = "Normal temperature."
#     else:
#         message = "Low temperature."
#     return message

# print(evaluate_temp_with_elif(36))
# print(evaluate_temp_with_elif(34))

# def get_taxes(earnings):
#     if earnings < 12000:
#         tax_owed = .25 * earnings
#     else:
#         tax_owed = .30 * earnings
#     return tax_owed

# ana_taxes = get_taxes(9000)
# yuri_taxes = get_taxes(15000)

# print(ana_taxes)
# print(yuri_taxes)

# def get_dose(weight):
#     # Dosage is 1.25 ml for anyone under 5.2 kg
#     if weight < 5.2:
#         dose = 1.25
#     elif weight < 7.9:
#         dose = 2.5
#     elif weight < 10.4:
#         dose = 3.75
#     elif weight < 15.9:
#         dose = 5
#     elif weight < 21.2:
#         dose = 7.5
#     # Dosage is 10 ml for anyone 21.2 kg or over
#     else:
#         dose = 10
#     return dose

# print(get_dose(12))


## Intro to Lists


# Organize your data so you can work with it efficiently.
# One way to do this is by organizing the names in a Python string.

flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"

print(type(flowers))
print(flowers)

# Even better is to represent the same data in a Python list. To create a list, you need to use square brackets ([, ]) and separate each item with a comma. Every item in the list is a Python string, so each is enclosed in quotation marks.

flowers_list = ["pink primrose", "hard-leaved procket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]

print(type(flowers_list))
print(flowers_list)

# Length

print(len(flowers_list))

# Indexing - We can refer to any item in the list according to its position in the list (first, second, third, etc).

print("First entry:", flowers_list[0])
print("second entry:", flowers_list[1])
print("Last entry:", flowers_list[9]) # The list has length ten, so we refer to final entry with 9

# Slicing

