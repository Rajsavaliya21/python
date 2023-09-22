# How will you compare two lists?

one=[1,2,3]
two=[1,2,3,4]
j="no"
for i,k in zip(one,two) :
    if i==k:
        j="yes"
        continue
    else:
        j="no"
        break
if j == "yes" and len(one)==len(two):
    print("it is same.")
else:
    print("it is not same")