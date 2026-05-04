a={x**2 for x in range(10)}

b={num for num in a if num>20 and num< 50}

print(a)
print(b)

lst=[a+b for a in [1,2, 3] for b in [3, 4, 5]]
print(lst)

lst1=[[a+b for a in [1,2,3]] for b in [3,4,5]]
print(lst1)
# generate all unique combinations of 1, 2 and 3
d = [(i, j, k) for i in [1,2,3] for j in [1,2,3] for k in [1, 2, 3] if i != j \
and j !=k and k != i]
print(d)