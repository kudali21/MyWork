#Vasuki kudali  pfs22

def rock_paper_scissors():
  return '''
  ***Rock Paper Scissors***

  import random

  choices = ["rock", "paper", "scissors"]
  user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
  computer_choice = random.choice(choices)

  print(f"Computer chose: {computer_choice}")

  if user_choice == computer_choice:
    print("It's a tie!")
  elif (user_choice == "rock" and computer_choice == "scissors") or \
    (user_choice == "paper" and computer_choice == "rock") or \
    (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
  else:
    print("You lose!")
  ==========================================
  Testcase-1:
  Enter your choice (rock, paper, or scissors): rock
  Computer chose: paper
  You lose!
  ------------------------------------------
  Testcase-2:
  Enter your choice (rock, paper, or scissors): paper
  Computer chose: rock
  You win!
  ==========================================
  '''
def area_of_cylinder():
  return '''
  ***Area of Cylinder***

  import math

  radius = float(input("Enter the radius of the cylinder: "))
  height = float(input("Enter the height of the cylinder: "))

  area = 2 * math.pi * radius * (radius + height)

  print(f"Surface area of the cylinder is: {area:.2f}")
  ==========================================
  Testcase-1:
  Enter the radius of the cylinder: 3
  Enter the height of the cylinder: 5
  Surface area of the cylinder is: 150.80
  ------------------------------------------
  Testcase-2:
  Enter the radius of the cylinder: 7
  Enter the height of the cylinder: 10
  Surface area of the cylinder is: 750.50
  ==========================================
  '''
def average_of_array():
  return '''
  ***Average of Array***

  arr = list(map(int, input("Enter numbers separated by space: ").split()))
  avg = sum(arr) / len(arr)
  print(f"The average is: {avg}")
  ==========================================
  Testcase-1:
  Enter numbers separated by space: 1 2 3 4 5
  The average is: 3.0
  ------------------------------------------
  Testcase-2:
  Enter numbers separated by space: 10 20 30
  The average is: 20.0
  ==========================================
  '''
def simple_calculator():
  return '''
  ***Simple Calculator***

  def add(x, y):
    return x + y

  def subtract(x, y):
    return x - y

  def multiply(x, y):
    return x * y

  def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

  print("Select operation:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")

  choice = input("Enter choice(1/2/3/4): ")

  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))

  if choice == '1':
    print(f"Result: {add(num1, num2)}")
  elif choice == '2':
    print(f"Result: {subtract(num1, num2)}")
  elif choice == '3':
    print(f"Result: {multiply(num1, num2)}")
  elif choice == '4':
    print(f"Result: {divide(num1, num2)}")
  else:
    print("Invalid input")
  ==========================================
  Testcase-1:
  Enter first number: 5
  Enter second number: 3
  Enter choice(1/2/3/4): 1
  Result: 8.0
  ------------------------------------------
  Testcase-2:
  Enter first number: 5
  Enter second number: 0
  Enter choice(1/2/3/4): 4
  Result: Cannot divide by zero
  ==========================================
  '''
def find_median_of_array():
  return '''
  ***Find Median of Array***

  arr = list(map(int, input("Enter numbers separated by space: ").split()))
  arr.sort()
  n = len(arr)

  if n % 2 == 1:
    median = arr[n // 2]
  else:
    median = (arr[n // 2 - 1] + arr[n // 2]) / 2

  print(f"The median is: {median}")
  ==========================================
  Testcase-1:
  Enter numbers separated by space: 1 3 2 4
  The median is: 2.5
  ------------------------------------------
  Testcase-2:
  Enter numbers separated by space: 5 1 3 4 2
  The median is: 3
  ==========================================
  '''
def move_zeros_right():
  return '''
  ***Move All Zeros to Right***

  arr = list(map(int, input("Enter numbers separated by space: ").split()))
  result = []
  zero_count = 0

  for num in arr:
    if num != 0:
      result.append(num)
    else:
      zero_count += 1

  for _ in range(zero_count):
    result.append(0)

  print(f"Array after moving zeros to the right: {result}")
  ==========================================
  Testcase-1:
  Enter numbers separated by space: 1 0 2 0 3
  Array after moving zeros to the right: [1, 2, 3, 0, 0]
  ------------------------------------------
  Testcase-2:
  Enter numbers separated by space: 0 0 0 1
  Array after moving zeros to the right: [1, 0, 0, 0]
  ==========================================
  '''

def sum_of_ap_series():
  return '''
  ***Sum of AP Series***

  a = int(input("Enter the first term: "))
  d = int(input("Enter the common difference: "))
  n = int(input("Enter the number of terms: "))

  sum_ap = n / 2 * (2 * a + (n - 1) * d)
  print(f"Sum of the AP series: {sum_ap}")
  ==========================================
  Testcase-1:
  Enter the first term: 1
  Enter the common difference: 2
  Enter the number of terms: 5
  Sum of the AP series: 25.0
  ------------------------------------------
  Testcase-2:
  Enter the first term: 3
  Enter the common difference: 4
  Enter the number of terms: 4
  Sum of the AP series: 38.0
  ==========================================
  '''
def sum_of_prime_numbers():
  return '''
  ***Sum of All Prime Numbers in Given Range***

  def is_prime(n):
      if n <= 1:
        return False
      for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
      return True

  start = int(input("Enter the start of the range: "))
  end = int(input("Enter the end of the range: "))

  prime_sum = sum(n for n in range(start, end+1) if is_prime(n))
  print(f"Sum of all prime numbers in the range: {prime_sum}")
  ==========================================
  Testcase-1:
  Enter the start of the range: 10
  Enter the end of the range: 20
  Sum of all prime numbers in the range: 60
  ------------------------------------------
  Testcase-2:
  Enter the start of the range: 1
  Enter the end of the range: 5
  Sum of all prime numbers in the range: 10
  ==========================================
  '''
def right_to_vote_greeting():
  return '''
  ***Right to Vote***

  age = int(input("Enter your age: "))

  if age >= 18:
    print("You are eligible to vote!")
  else:
    print("You are not eligible to vote yet.")
  ==========================================
  Testcase-1:
  Enter your age: 20
  You are eligible to vote!
  ------------------------------------------
  Testcase-2:
  Enter your age: 16
  You are not eligible to vote yet.
  ==========================================
  '''
def pounds_to_kgs():
  return '''
  ***Pounds to Kgs***

  pounds = float(input("Enter weight in pounds: "))
  kgs = pounds * 0.453592
  print(f"Weight in kilograms: {kgs:.2f}")
  ==========================================
  Testcase-1:
  Enter weight in pounds: 150
  Weight in kilograms: 68.18
  ------------------------------------------
  Testcase-2:
  Enter weight in pounds: 200
  Weight in kilograms: 90.72
  ==========================================
  '''
def simple_interest():
  return '''
  ***Simple Interest***

  p = float(input("Enter principal amount: "))
  r = float(input("Enter rate of interest: "))
  t = float(input("Enter time in years: "))

  si = (p * r * t) / 100
  print(f"Simple interest is: {si}")
  ==========================================
  Testcase-1:
  Enter principal amount: 1000
  Enter rate of interest: 5
  Enter time in years: 2
  Simple interest is: 100.0
  ------------------------------------------
  Testcase-2:
  Enter principal amount: 1500
  Enter rate of interest: 4
  Enter time in years: 3
  Simple interest is: 180.0
  ==========================================
  '''
def cubes():
  return '''
  ***Cubes of Numbers***

  n = int(input("Enter a number: "))
  cube = n ** 3
  print(f"The cube of {n} is: {cube}")
  ==========================================
  Testcase-1:
  Enter a number: 3
  The cube of 3 is: 27
  ------------------------------------------
  Testcase-2:
  Enter a number: 4
  The cube of 4 is: 64
  ==========================================
  '''
def display_calendar():
  return '''
  ***Display Calendar***

  import calendar

  year = int(input("Enter year: "))
  month = int(input("Enter month (1-12): "))

  print(calendar.month(year, month))
  ==========================================
  Testcase-1:
  Enter year: 2025
  Enter month (1-12): 5
  (Calendar for May 2025)
  ------------------------------------------
  Testcase-2:
  Enter year: 2024
  Enter month (1-12): 12
  (Calendar for December 2024)
  ==========================================
  '''
def split_and_join():
  return '''
  ***Split and Join a String***

  s = input("Enter a string: ")
  split_string = s.split()
  joined_string = "-".join(split_string)
  print(f"String after split and join: {joined_string}")
  ==========================================
  Testcase-1:
  Enter a string: hello world
  String after split and join: hello-world
  ------------------------------------------
  Testcase-2:
  Enter a string: python programming
  String after split and join: python-programming
  ==========================================
  '''
def generate_random_number():
  return '''
  ***Generate a Random Number***

  import random

  rand_num = random.randint(1, 100)
  print(f"Random number between 1 and 100: {rand_num}")
  ==========================================
  Testcase-1:
  Random number between 1 and 100: 45
  ------------------------------------------
  Testcase-2:
  Random number between 1 and 100: 87
  ==========================================
  '''
def ascii_value():
  return '''
  ***Find ASCII Value of Character***

  char = input("Enter a character: ")
  ascii_val = ord(char)
  print(f"ASCII value of {char} is: {ascii_val}")
  ==========================================
  Testcase-1:
  Enter a character: A
  ASCII value of A is: 65
  ------------------------------------------
  Testcase-2:
  Enter a character: z
  ASCII value of z is: 122
  ==========================================
  '''
def non_repeating_char():
  return '''
  ***Find Non-Repeating Character of String***

  s = input("Enter a string: ")

  for char in s:
      if s.count(char) == 1:
          print(f"First non-repeating character: {char}")
          break
  ==========================================
  Testcase-1:
  Enter a string: swiss
  First non-repeating character: w
  ------------------------------------------
  Testcase-2:
  Enter a string: hello
  First non-repeating character: h
  ==========================================
  '''
def days_between_dates():
  return '''
  ***Days Between Two Dates***

  from datetime import datetime

  date_format = "%Y-%m-%d"
  date1 = input("Enter the first date (YYYY-MM-DD): ")
  date2 = input("Enter the second date (YYYY-MM-DD): ")

  d1 = datetime.strptime(date1, date_format)
  d2 = datetime.strptime(date2, date_format)

  diff = (d2 - d1).days
  print(f"Days between {date1} and {date2}: {diff} days")
  ==========================================
  Testcase-1:
  Enter the first date (YYYY-MM-DD): 2025-05-01
  Enter the second date (YYYY-MM-DD): 2025-05-07
  Days between 2025-05-01 and 2025-05-07: 6 days
  ------------------------------------------
  Testcase-2:
  Enter the first date (YYYY-MM-DD): 2024-12-01
  Enter the second date (YYYY-MM-DD): 2024-12-25
  Days between 2024-12-01 and 2024-12-25: 24 days
  ==========================================
  '''
def hello_python():
  return '''
  ***Print Hello Python***

  print("Hello Python")
  ==========================================
  Testcase-1:
  Output: Hello Python
  ------------------------------------------
  Testcase-2:
  Output: Hello Python
  ==========================================
  '''
