# Write a Python function that takes a list and returns a new list with unique elements from the first list.
new_list=list()
list_k=[1,1,2,2,3,3,4,4,55,55,5,6,6,6]
def unique(lisd):
    for i in lisd:
        if i not in new_list:
            new_list.append(i)
    print(new_list)

unique(list_k)
