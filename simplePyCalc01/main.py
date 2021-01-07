#addition
def add(input1, input2):
    result = input1 + input2
    print(input1, " + ", input2 , " = ")
    print(result)

#subtraction
def subtract(input1, input2):
    result1 = input1 - input2
    print(input1 , " - " , input2 , " = ")
    print(result1)

#multiply
def multiply(input1, input2):
    result2 = input1 * input2
    print(input1 , " * " , input2 , " = ")
    print(result2)

# division
def divide(input1, input2):
    if input2 == 0:
        print("numbers can 'NOT' be divided by ZERO")
    else:
        result3= input1 / input2
        print(input1 , " / " , input2 , " = ")
        print(result3)

def main():
    print("""
    This is a basic calculator app it will do:
    addition,
    subtraction,
    division,
    and multiplication.
    Please enter two numbers (they can be integers or floats)
    """)
    while True:
        try:
            input1 = float(input("> ").strip())
            input2 = float(input("> ").strip())
            break
        except ValueError:
            print("Invalid Entry, not a Float or Integer... Try Again")

    print("""
         Now do you want to 
         A) Add
         S) Substract
         M) Multiply
         D) Divide
         the numbers?
         """)

    while True:
      input3 = str(input("> ").strip().lower())
      if input3 == "a":
        add(input1, input2)
        break
      elif input3 == "s":
        subtract(input1, input2)
        break
      elif input3 == "m":
        multiply(input1, input2)
        break
      elif input3 == "d":
        divide(input1, input2)
        break
      else:
        print("Not a valid entry")

main()