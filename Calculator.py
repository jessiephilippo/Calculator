#Made by Jessie Philippo
#2-3-2020
#version 3

#make the function for the calculator.
def calculator():
    print("     Calculator    ")
    print()
    
    #set the variables as inputs and as float. except for op
    #runs trough the while loop if num1 == a number then it will break out of the while loop and continues
    while True:
        try:
            num1 = float(input("Enter first number: "))
            break
        #if the while == false this will be printed
        except:
            print("Only numbers: ")
            
    while True:
        try:
            operators = ["x","X","*"]
            op = input("Enter operator: ")
            if op in operators:
                break
        except:
            print("invalid operators")
    
    while True:
        try:
            num2 = float(input("Enter second number: "))
            break
        except:
            print("Only numbers: ")

    #the if statement so that it can recognize the different operators that exists.
    if op == "+":
        print()
        print(num1 + num2)
        
    elif op == "-":
        print()
        print(num1 - num2)
        
    elif op == "x" or op == "X" or  op == "*":
        print()
        print(num1 * num2)
        
    elif op == "/":
        print()
        print(num1 / num2)

#making the main so i can put the calculator funtion in the main.
def main():
    calculator()

#runs the program
if __name__ == '__main__':
        main()
