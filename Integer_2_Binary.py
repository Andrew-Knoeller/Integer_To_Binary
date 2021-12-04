user_Num = int(input ("Please enter a number to convert to binary: "))
conversion_List = []
while user_Num > 0:
    bin_Num = user_Num % 2
    conversion_List.append(bin_Num)
    user_Num = user_Num // 2
conversion_List.reverse()
print("Your number in binary form is: ")
for i in conversion_List:
    print(i, end="")

input('\n\n\nPress Enter to exit')