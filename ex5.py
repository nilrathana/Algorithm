# Ex5 - String
# We have text = "454639"
# Q1 - Count odd and even number in text
# Q2 - Sum all number
# Q3 - Sum only even number
# Q4 - Reverse

#Q1:
text = "454639"
even_number = 0
odd_number = 0
for i in range (len(text)):
    if int(text[i]) %2==0:
       even_number += 1
    else:
        odd_number += 1
print(even_number,odd_number) 
#Q2:
text = "454639"
sum = 0
for i in range (len(text)):
    sum += int(text[i])
print(sum)
# Q3:
text = "454639"
sum = 0
for i in range (len(text)):
    if int(text[i])%2 ==0:
        sum += int(text[i])
print("total:",sum)
#Q4:
text = "454639"
result = ""
for i in range (len(text)):
    reversed = (len(text))-1
    result += text[reversed-i]
print(result)
