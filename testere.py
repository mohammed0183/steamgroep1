# input a number
try:
  num = int(input("Enter an integer number: "))
  print("num:", num)
except ValueError:
    print("Please input integer only...")
