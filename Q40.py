# Write a Python script to merge two Python dictionaries.

d_1 = {"a": 100, "b": 200, "c": 300}
d_2 = {"a": 300, "b": 200, "d": 400}
final=dict()
for keyy in d_1:
    for keyy1 in d_2:
        if keyy==keyy1:
            final[keyy]=d_1[keyy]+d_2[keyy1]
        elif d_1[keyy] not in final and d_1[keyy]!=d_2[keyy1]:
            final[keyy]=d_1[keyy]
            final[keyy1]=d_2[keyy1]
print(final)
