## Standard Libraries in Python ##

## 1. Math Library

import math

# Constants
print("Pi:", math.pi)
print("Euler's number:", math.e)

# Functions
print("Square root of 16:", math.sqrt(24))
print("Factorial of 5:", math.factorial(5))
print("Cosine of 45 degrees:", math.cos(math.radians(45)))

# print(help(math))

print ("\n")

## 2. DateTime

from datetime import datetime, timedelta

# Current date and time
now1 = datetime.now()
print("Current date and time:", now1)

# Formatting dates
formatted_date = now1.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date:", formatted_date)

# Adding days to a date
future_date = now1 + timedelta(days=5)
print("Date after 5 days:", future_date)

print("\n")

## 3. OS Module

import os

# Get current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# List files in a directory
files = os.listdir(cwd)
print("Files in current directory:", files)

# Create and remove a directory
os.mkdir("test_directory")
print("Directory created.")
os.rmdir("test_directory")
print("Directory removed.")

# help(os.mkdir)

print("\n")


## 4. Random Module

import random

# Random float between 0 and 1
print("Random float:", random.random())

# Random integer between 10 and 50
print("Random integer:", random.randint(10, 50))

# Random choice from a list
choices = ['red', 'blue', 'green', 'yellow']
print("Random choice:", random.choice(choices))

# Shuffle a list
random.shuffle(choices)
print("Shuffled list:", choices)



# Parameters
start = 10  # Lower bound
end = 50    # Upper bound
size = 10   # Number of elements in the list

# Generate a list of random integers
random_integers = [random.randint(start, end) for _ in range(size)]
print("Random integers:", random_integers)

print("\n")

## 5. Json Module

import json

# Python dictionary to JSON string
data = {"name": "John", "age": 30, "city": "New York"}
json_string = json.dumps(data)
print("JSON string:", json_string, type(json_string))

# JSON string to Python dictionary
parsed_data = json.loads(json_string)
print("Parsed dictionary:", parsed_data, type(parsed_data))

#print(help(json))

print("\n")


## 6. Sys Module

import sys

# Command-line arguments
print("Command-line arguments:", sys.argv)

# Python version
print("Python version:", sys.version)

# Exit the program
# sys.exit("Exiting the program...")


# Creating your own custom module and using it as a module/library 

import sys,os

sys.path.append("c:/Users/aruni/OneDrive/Documents/JetLearn/Advanced_python_programming")
import math_utils as math_custom 

result1 = math_custom.addition(5,2)  
result2 = math_custom.subtraction(5,2)  
result3 = math_custom.division(5,2)
result4 = math_custom.multiplication(5,2)   
result5 = math_custom.quotient(5,2)  
result6 = math_custom.remainder(5,2)   
result7 = math_custom.pi 

print("Output of addition operation is :", result1)
print("Output of subtraction operation is :", result2) 
print("Output of division operation is :", result3) 
print("Output of multiplication operation is :", result4) 
print("Output of quotient operation is :", result5) 
print("Output of remainder operation is :", result6)  
print("Output of Pi operation is :", result7)  









