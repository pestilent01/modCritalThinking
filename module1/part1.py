from shared.getInput import getInput

def calculateTwoNumbers(num1, num2):
    return num1 + num2, num1 - num2


def main():
    
    num1 = getInput("Enter first number: ")
    num2 = getInput("Enter second number: ")

    addResult, subResult = calculateTwoNumbers(num1, num2)
    print("Add result: ", addResult)
    print("Sub result: ", subResult)

if __name__ == "__main__":
    main()