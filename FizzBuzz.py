# Problem 1 - FizzBuzz
def fizzbuzz():

    for i in range(1, 101):
        # A number is fizz if it is divisible by 3 or if it has a 3 in it 
        # A number is buzz if it is divisible by 5 or if it has a 5 in it 
        if "3" in str(i) and "5" in str(i):
            print("FizzBuzz")
        elif "3" in str(i):
            print("Fizz")
        elif "5" in str(i):
            print("Buzz")
        else:
            # For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
            # For numbers which are multiples of both three and five print "FizzBuzz". 
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)

