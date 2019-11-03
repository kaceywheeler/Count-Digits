#Kacey Wheeler
#AP Computer Science: 2A
#2/19/19
#Unit 8 Labs
#Count Digits

num = int(input("Enter an integer: "))
count = 0
while (num > 0):
    num = num // 10
    count = count + 1

print(count)
