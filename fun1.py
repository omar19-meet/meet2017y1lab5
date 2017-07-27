####
##def add_numbers(): #This function adds all numbers from 1 to 100 and gives us the sum at the end
##    c=0
##    for number in range(1,100+1):
##        print(number)
##        c=c+number
##    return (c)
##answer= add_numbers()
##print(answer)




##start=int(input("What is your starting number? "))
##end= int(input("What is your ending number? "))
def add_numbers(start, end):
    c=0
    for number in range(start, end +1):
##        print(number)
        c=c+number
    return (c)
##answer= add_numbers(start, end)
##print(answer)

test1= add_numbers(1,2)
print(test1)

test2= add_numbers(1,100)
print(test2)

test3=add_numbers(1000,5000)
print(test3)
