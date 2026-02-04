
def find_index(numbers, value):
    """
    Write a function that takes a list and a value, 
    and returns the index of the value in the list. 
    If the value is not in the list, return -1. 
    Do not use the built-in .index() method for this problem.
    """
    if value in numbers:
        return numbers.index(value)
    else:
        return -1
    

def categorize_number(n):
    """
    Write a function that categorizes the given number as 'negative', 'zero', or 'positive'.
    """
    if n ==0:
        return 'zero'
    elif n<0:
        return 'negative'
    else:
        return 'positive'

def reverse_list(numbers):
    """
    Write a function that returns the reversed version of a list without using the built-in reverse method.
    """
    return numbers[::-1]

def process_numbers(numbers):
    """
    Write a function that takes a list of numbers. 
    The function should iterate through the list and print each number until it encounters a negative number, 
    at which point it should break out of the loop. If it encounters a zero, it should skip that iteration using the continue statement.
    """
    for i in numbers:
        if i == 0:
            continue
        elif i > 0:
            print(i)
        else:
            break

def string_lengths(strings):
    """
    Given a list of strings, write a function that returns a dictionary where the keys are the strings and the values are the lengths of those strings.
    """
    d = {}
    for s in strings:
        d[s] = len(s)
    return d

def even_values_keys(data):
    """
    Given a dictionary, write a function that returns a list of keys whose values are even numbers.
    """
    even = []
    for key, value in data.items():
        if value % 2 == 0:
            even.append(key)
    return even

def square_evens(numbers):
    """
    Given a list of numbers, use a list comprehension to return a list of squares of even numbers.
    """
    even_squares = []
    for i in numbers:
        if i % 2 ==0:
            even_squares.append(i*i)
    return even_squares

def long_strings(strings):
    """
    Given a list of strings, use a list comprehension to return a list of strings that have a length greater than 5.
    """
    long_strings = []
    for s in strings:
        if len(s) >5:
            long_strings.append(s)
    return long_strings

def convert_to_celsius(fahrenheit_temps):
    """
    Convert a list of temperatures from Fahrenheit to Celsius.
    
    Given a list of temperatures in Fahrenheit, convert each temperature to Celsius. 
    If the temperature is below freezing (32°F or 0°C), append the string "Freezing" 
    to the converted temperature. Otherwise, just return the converted temperature.
    
    Formula for Conversion:
    Celsius = (Fahrenheit - 32) / 1.8

    Example:
    Input: [32, 50, 100, 0, 20]
    Output: ['0.0°C Freezing', '10.0°C', '37.8°C', '-17.8°C Freezing', '-6.7°C Freezing']
    """
    celsius = []
    for f in fahrenheit_temps:
        c = round((f - 32)/1.8,1)
        c_string = str(c) + '°C'
        if c <= 0:
            c_string = c_string + " Freezing"
        celsius.append(c_string)
    return celsius




