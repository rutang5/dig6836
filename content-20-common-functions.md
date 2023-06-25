# 20 Common Python Functions

In Python, functions are blocks of reusable code that perform specific tasks. They help in organizing and modularizing your code, making it easier to read and maintain. Here are 20 common Python functions along with examples to demonstrate their usage.

## 1. `print()`

The `print()` function is used to display output on the console.

```python
print("Hello, World!")
```

## 2. `len()`

The `len()` function returns the length of a sequence, such as a string, list, or tuple.

```python
name = "John Doe"
print(len(name))
```

## 3. `input()`

The `input()` function allows the user to enter values from the console.

```python
name = input("Enter your name: ")
print("Hello,", name)
```

## 4. `int()`

The `int()` function converts a value to an integer.

```python
number = int("42")
print(number)
```

## 5. `float()`

The `float()` function converts a value to a floating-point number.

```python
pi = float("3.14")
print(pi)
```

## 6. `str()`

The `str()` function converts a value to a string.

```python
age = 25
print("I am " + str(age) + " years old.")
```

## 7. `range()`

The `range()` function generates a sequence of numbers within a specified range.

```python
for num in range(1, 5):
    print(num)
```

## 8. `list()`

The `list()` function creates a list from an iterable object.

```python
numbers = list(range(1, 5))
print(numbers)
```

## 9. `tuple()`

The `tuple()` function creates a tuple from an iterable object.

```python
coordinates = tuple([3, 4])
print(coordinates)
```

## 10. `dict()`

The `dict()` function creates a dictionary from a sequence of key-value pairs.

```python
person = dict(name="John", age=30)
print(person)
```

## 11. `sorted()`

The `sorted()` function returns a new sorted list from an iterable object.

```python
numbers = [5, 2, 8, 1, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
```

## 12. `max()`

The `max()` function returns the largest item in an iterable or the largest of two or more arguments.

```python
numbers = [5, 2, 8, 1, 3]
maximum = max(numbers)
print(maximum)
```

## 13. `min()`

The `min()` function returns the smallest item in an iterable or the smallest of two or more arguments.

```python
numbers = [5, 2, 8, 1, 3]
minimum = min(numbers)
print(minimum)
```

## 14. `sum()`

The `sum()` function returns the sum of all items in an iterable.

```python
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)
```

## 15. `abs()`

The `abs()` function returns the absolute value of a number.

```python
number = -5
absolute_value = abs(number)
print(absolute_value)
```

## 16. `round()`

The `round()` function returns a rounded version of a floating-point number.

```python
pi = 3.14159
rounded_pi = round(pi, 2)
print

(rounded_pi)
```

## 17. `type()`

The `type()` function returns the type of an object.

```python
name = "John"
print(type(name))
```

## 18. `isinstance()`

The `isinstance()` function checks if an object is an instance of a specified class.

```python
number = 42
print(isinstance(number, int))
```

## 19. `zip()`

The `zip()` function returns an iterator that combines multiple iterables into tuples.

```python
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
print(list(zipped))
```

## 20. `help()`

The `help()` function displays the documentation and help messages for Python objects.

```python
help(print)
```

These are just a few examples of commonly used Python functions. Python provides a rich library of built-in functions and allows you to define your own custom functions to suit your specific needs.
