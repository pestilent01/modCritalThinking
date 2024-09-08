'''
Part 2:
The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased each month. The points are awarded as follows:

If a customer purchases 0 books, they earn 0 points.
If a customer purchases 2 books, they earn 5 points.
If a customer purchases 4 books, they earn 15 points.
If a customer purchases 6 books, they earn 30 points.
If a customer purchases 8 or more books, they earn 60 points.
Write a program that asks the user to enter the number of books that they have purchased this month and then display the number of points awarded.

'''

numBooks = int(input("Enter the number of books purchased this month: \n"))
earnedPoints = 0
pointLookup = {0:0,1:0,2:5,3:5,4:15,5:15,6:30,7:30}

while numBooks < 0:
    numBooks = int(input("Invalid input. Please enter a positive number.\n"))

if numBooks >= 8:
    earnedPoints = 60
else:
    earnedPoints = pointLookup[numBooks]


print(f"You have purchased {numBooks} books and earned {earnedPoints} points this month.")
