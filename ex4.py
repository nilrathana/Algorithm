# # Ex4 - String
# We have text = "3 4 5 6"
# Q1 - display number 1 by one without space
# Q2 - Sum all number (Total: 18)
#Q1:
text = " 3 4 5 6"
for i in text:
  if i != "":
     print(i)

#Q2:
text = input("Enter your number : ")
sum = 0 
n = " "
for i in range(len(text)) :
    if text[i] == " ":
        n+= ""
    else: 
        n += text[i]
        sum += int(text[i])
print("Total :", sum)


