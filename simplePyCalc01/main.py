#addition 



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
        input1 = float(input("> ").strip())
        input2 = float(input("> ").strip())

    print("""
         Now do you want to 
         A) add
         S) substract
         M) multiply
         D) divide
         the numbers?
         """)

    while True:
      input3 = str(input("> ").strip().lower())
      if input3 == "a":
           add(input1, input2)

        elif input3 == "s":
            subtract(input1, input2)

        elif input3 == "m":
            multiply(input1, input2)

        elif input3 == "d":
            divide(input1, input2)

        else:
            print("Not a valid entry")
