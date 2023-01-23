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

# Using Multiple Variables
num_years = 4
days_per_year = 365
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60

# Calculate the number of seconds in four years

total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs)

# Update to include leap years - devemos escrever a equacao novamente apos atualizar a variavel days_per_year
days_per_year = 365.25
total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs)

my_income = 1000 # salario
tax_rate = 0.15 # 15% de impostos 
may_taxes = my_income * tax_rate
print(may_taxes)

## Introduction to Strings
