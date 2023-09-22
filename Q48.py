# Write a Python program to combine values in a Python list of 
# dictionaries. Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}] Expected Output: Counter({'item1': 1150, 'item2': 300})

l=[{'item':'item1','amount':400},{'item':'item2','amount':300},{'item': 'item1', 'amount': 750}]


from collections import Counter

coll = Counter()

for i in l:
    # items = i['item']
    # amount=i['amount']
    coll [i['item']]+= i['amount']
print(coll)

