
#Part 1:
#Write a program that calculates the total amount of a meal purchased 
# at a restaurant. The program should ask the user to enter the charge
# for the food and then calculate the amounts with an 18 percent tip 
# and 7 percent sales tax. Display each of these amounts and the total price.

def calculateTip(amount, tipRate):
    return amount * tipRate

def calculateTax(amount, taxRate):
    return amount*taxRate

def calculateTotal(meal,tax,tip):
    return meal+tax+tip

taxRate = 0.07
tipRate = 0.18

print("What is the amount of the of meal")
mealTotal = float(input())

tax = calculateTax(mealTotal, taxRate) #calculate the tax
tip = calculateTip(mealTotal, tipRate) #calculate the tip

grandTotal =  calculateTotal(mealTotal, tax,tip) #calculate the total.

#print out the results
print("Meal Amount: ${:.2f}".format(mealTotal))
print("Tax({:.2f}%): ${:.2f}".format(taxRate*100.0, taxRate*mealTotal))
print("Tip ({:.2f}%) ${:.2f}".format(tipRate*100.0, tipRate*mealTotal))
print("Grand Total: ${:.2f}".format(grandTotal))