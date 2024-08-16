# Ex7 - number
# Enter number in range 10 - 20 until you enter other number out of range
# display "Continue" if number in range 10 - 20
# display "Out of range" if number difference from range 10 - 20
numbers = input("Enter number:")
result = ""
for i in range (len(numbers)):
    if i <=10 and i <=20:
        result = "continue"
    else:
        result ="Out of range"
        print(result)