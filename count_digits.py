#Kacey Wheeler
#AP Computer Science: 2A
#2/19/19
#Unit 8 Labs
#Count Digits

#Get integer from user
num = int(input("Enter an integer: "))
#Set count equal to 0
count = 0
#While num is greater than 0
while (num > 0):
    #Adds one to count for each digit
    num = num // 10
    count = count + 1

#Print the number of digits 
print(count)
