import random
a=[random.randint(10, 100) for n in range(20)]
#generates 20 random ints b/w 10 and 100
a1=[(x,x**2, x**3)for x in range(10)]
print(a, a1)

#convert a list of strings to a list of integers 
b=[int(x) for x in ['10', '20', '30', 40]]
print(b)


#generate the list of even numbers in range(10 to 30)
c=[n for n in range (10, 30) if n%2==0]

print(c)

#from list of all numbers delete numbers having value 20 and 50
d=[num for num in a if num<20 or num>50]
print(d)

#when if-else both are used, place them before for 
#replace a vowel in a string with !
e=['!' if alphabet in 'aeiou' else alphabet for alphabet in 'Technical']
print(e)

#flatten a list of list
arr=[[1, 2, 3, 4], [5, 6, 7, 8],[10, 11, 12, 13]]
f=[n for ele in arr for n in ele]
print(f)

#* can be used to unpack a list 
g=[*arr[0], *arr[1], *arr[2]]
print(g)