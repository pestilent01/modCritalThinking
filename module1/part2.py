from shared.getInput import getInput

def validValue(num):
    return num > 0

def multiplyNumbers(num1, num2):
    return num1 * num2
def divideNumbers(num1, num2):
    return num1 / num2

def main():

    input("Multiply two numbers. Press Enter to continue")
    num1 = getInput("Enter first number: ")
    num2 = getInput("Enter second number: ")
    multResult = multiplyNumbers(num1, num2)
    print("Multiplication result of {0} X {1} is ".format(num1, num2), multResult)

    input("Divide first number by second number. Press Enter to continue")
    while(num2==0):
        print("Second number must not be zero")
        num2 = getInput("Enter second number: ");
        if not validValue(num2):
            print("Only non-zero value is allowed")
            
    divResult = divideNumbers(num1, num2)
    print("Division result of {0} / {1} is  ".format(num1, num2), divResult)

if __name__ == "__main__":
    main()
