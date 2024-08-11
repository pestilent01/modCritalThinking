def getInput(message):
   num = 0
   while(True):
       print(message)
       try:
           num = int(input())
           return num
       except ValueError:
           print("Only numeric values are allowed")
