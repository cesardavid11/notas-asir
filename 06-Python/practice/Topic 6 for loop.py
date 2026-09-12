# for loops = execute a block of code a fixed number of times.
#             you can interate over a range, string, secuence, etc.

#for i in range(1, 11):
#    print(i)


#for i in reversed(range(1, 11)):
#    print(i)
#print("HAPPY NEW YEAR!")


#credit_card = "1234-5678-9012-3456"

#for x in credit_card:
#    print(x)

#for i in range(1, 21):
#    if i == 13:
#        continue
#    else:
#        print(i)

for number in range(1, 10):
    if number == 5:
        break  
    print(number)
else:
    print("Loop finished completely!") 