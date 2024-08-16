# Ex10 - Number
# Enter 5 numbers and find maximum and minimum value
# Example:
# 1
# 5
# 6
# 7
# 0
# output : Max = 7, Min = 0
#Ex10:
combo=""
for i in range (5):
   number = int(input("Enter number:"))
   combo += str(number)
print(combo)
max = 0
min = 0
for i in range (len(combo)):
  if int(combo[i]) > max:
    max = int(combo[i])
if int(combo[i]) < min:
    min = int(combo[i])
print("max",max,"min",min)