# # Beginner Level
# ### 1. Print Numbers
# Print numbers from 1 to 10 using a `for` loop.

# for i in range(1,11):
#     print(i)
# ---

# ### 2. Print Even Numbers
# Print all even numbers between 1 and 20.

# for i in range(1,21):
#     if i % 2 == 0 :
#         print(i)
# ---

# ### 3. Print a Name 5 Times
# Take a name from the user and print it 5 times.

# user = input("Enter name: ")
# for i in range(5):
#     print(user)
# ---

# ### 4. Sum of Numbers
# Find the sum of numbers from 1 to 100.

# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)
# ---

# ### 5. Multiplication Table
# Take a number from the user and print its table.

# num = int(input("Enter number: "))
# for i in range(1,11):
#     print(f"{num} x {i} = {num * i}")
# ---

# # Intermediate Level
# ### 6. Count Vowels
# Take a string and count how many vowels are present using a `for` loop.

# string = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# count = 0
# for char in string:
#     if char in vowels:
#         count += 1
# print(count)
# ---

# ### 7. Reverse a String
# Take a string and reverse it using a `for` loop.

# string = input("enter the string: ")
# rev_str = " "
# for i in string:
#     rev_str = i + rev_str
#     print(rev_str)
# ---

# ### 8. Factorial of a Number
# Take a number and find its factorial.

# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print(factorial)
# ---

# ### 9. Count Digits
# Take a number and count its digits using a loop.

# num = int(input("Enter a number: "))
# count = 0
# for i in str(num):
#     count += 1 
# print(count)
# ---

# ### 10. Find Largest Number
# Find the largest number using a `for` loop.

# numbers = [12, 45, 2, 89, 34]
# largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
# print(largest)
# ---

# # Pattern Questions
# ### 11. Star Pattern
# *
# **
# ***
# ****
# *****

# for i in range (1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print() 
# ---


# ### 12. Reverse Star Pattern
# *****
# ****
# ***
# **
# *

# for i in range(5,0,-1):
#     for j in range(1 , i + 1):
#         print("*",end="")
#     print()
# ---

# ### 13. Number Pattern
# 1
# 12
# 123
# 1234
# 12345

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# ---

# # Real-World Practice
# ### 14. Expense Tracker
# Calculate total expenses using a `for` loop.

# expenses = [500, 200, 1000, 300, 150]
# total_exp = 0
# for exp in expenses:
#     total_exp += exp
# print(total_exp)
# ---

# ### 15. Student Marks
# Given:
# marks = [78, 85, 67, 90, 88]

# Find:
# * Total marks
# * Average marks
# * Highest marks
# using only `for` loops.

# marks = [78, 85, 67, 90, 88]
# total = 0
# for mark in marks:
#     total += mark
# average = total / len(marks)
# highest = marks[0]
# for mark in marks:
#     if mark > highest:
#         highest = mark
# print(f"Total Marks: {total}")
# print(f"Average Marks: {average}")
# print(f"Highest Marks: {highest}")

# ---

# # Challenge Questions
# ### 16. Prime Number Checker
# Take a number from the user and check whether it is prime.

# num = int(input("Enter number: "))

# for i in range(2, num):
#     if num % i == 0:
#         print("Not Prime")
#         break
# else:
#     print("Prime")

# ---

# ### 17. Fibonacci Series
# Print first `n` Fibonacci numbers.

# **Example (n=7):**

# ```python
# 0 1 1 2 3 5 8
# ```
# num = int(input("Enter n: "))
# a , b = 0 , 1 
# for i in range(num):
#     print(a , end=" ")
#     a , b = b , a + b

# ---

# ### 18. Armstrong Number
# Check whether a number is Armstrong or not.

# **Example:**

# ```python
# 153
# ```

# **Output:**

# ```python
# Armstrong Number
# ```

# num = int(input("Enter number: "))
# sum = 0
# for i in str(num):
#     sum += int(i) ** 3
# if sum == num:
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong Number")

# ---

# ### 19. Password Strength Checker

# Take a password and count:

# * Uppercase letters
# * Lowercase letters
# * Digits
# * Special characters

# using a `for` loop.

# password = input("Enter password: ")
# uppercase = 0
# lowercase = 0
# digits = 0
# special = 0
# for char in password:
#     if char.isupper():
#         uppercase += 1
#     elif char.islower():
#         lowercase += 1
#     elif char.isdigit():
#         digits += 1
#     else:
#         special += 1
# print(f"Uppercase: {uppercase}")
# print(f"Lowercase: {lowercase}")
# print(f"Digits: {digits}")
# print(f"Special Characters: {special}")

# ---

### 20. Mini Project

# Create a menu:

# ```python
# 1. Print Numbers
# 2. Sum of Numbers
# 3. Multiplication Table
# 4. Exit
# ```
# Use a `for` loop wherever needed.

# menu = """ 
# 1. Print Numbers
# 2. Sum of Numbers
# 3. Multiplication Table
# 4. Exit
# """
# while True:
    # print(menu)
    # choice = int(input("Enter your choice: "))
    # if choice == 1:
    #     for i in range(1, 11):
    #         print(i)
    # elif choice == 2:
    #     sum = 0
    #     for i in range(1, 101):
    #         sum += i
    #     print(f"Sum of numbers from 1 to 100 is: {sum}")
    # elif choice == 3:
    #     num = int(input("Enter number: "))
    #     for i in range(1, 11):
    #         print(f"{num} x {i} = {num * i}")
    # elif choice == 4:
    #     print("Exiting...")
    #     break
    # else:
    #     print("Invalid choice. Please try again.")

