# Write a Python function that takes two lists and returns true if they have at least one common member.

one=[1,2,3]
two=[4,5,1]
j="no"
for i in one :
    for k in two:
        if i==k:
            j="yes"
            continue
if j == "yes" :
    print("it is same.")
else:
    print("it is not same")