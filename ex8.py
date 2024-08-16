# Ex8 - String
# We have text = "9394884039"
# Q1 - How many number 8 in string
# Q2 - What is first index of letter 8
#Q1:
text = "9394884039"
count=0
for i in range (len(text)):
    if text[i] == "8":
        count +=1
print(count)
#Q2:
text = "9394884039"
is_found = False
for i in range (len(text)):
    if text[i]== "8" and not is_found ==True:
        print(i)
        is_found=True

    

