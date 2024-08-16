# Ex9 - String
# We have string = "3 4 5 6"
# Q1 - Remove space and keep result = "3456"
# Q2 - Multiple each letter by 2 result = "6 8 10 12"
#Q1:
text = "3 4 5 6"
result =""
for i in text:
    if i != " ":
      result += i
print(result)
#Q2:
text = "3 4 5 6"
result = ""
for i in range (len(text)):
    if text[i] !=" ":
        result += str(int(text[i])*2)+" "
print(result)

