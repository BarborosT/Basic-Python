
"""
1- Write a function that flattens a list. Its elements can consist of multi-layered lists (such as [[3],2]) or non-scalar data. For example:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]

"""


a = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
a1 = []

def flatten(n):
    for i in n:
        if isinstance(i,list):
            flatten(i)
        else:
            a1.append(i)
flatten(a)
print(a1)