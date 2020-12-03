from random import choice

numbers=[]
for i in range(1,76):
    numbers.append(i)

cont='Y'
printed_number=[]
print("Welcome to Bingo Game !!!")
while len(numbers)!=0:
    
    if cont.upper()=='Y':
        random_number=choice(numbers)
        print("Your new number is:",random_number)
        printed_number.append(random_number)
        numbers.remove(random_number)
        print("The number displayed so far is:", sorted(printed_number))                        
    elif cont.upper()=='N':
        break
    else:
        print("Please enter Y and N only")
    cont=input('Press Y to continue and N to exit the game: ')


print("Thank you for playing the game !!! \nHope to see you soon ")
    







