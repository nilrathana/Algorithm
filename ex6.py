# Ex6 - Number
# Enter number and check 
# if odd number print "Odd" otherwise print "Even"

#Ex6:
numbers =input("Enter number:")
odd = 0
even =0
for i in range (len(numbers)):
    if int(numbers[i])%2==1:
        odd = "odd_number"
    else:
        even = "even_number"
print(odd,even)
