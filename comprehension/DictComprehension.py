d={'a':1, 'b':2, 'c':3, 'd':4}
#obtain dictionary with each value cubed
d1={k:v**3 for (k,v) in d.items()}
print(d1)

d2={k:v**3 for (k, v) in d.items() if v >3}
print(d2)
d3={k:('Even' if v%2==0 else 'Odd') for (k,v) in d.items()}
print(d3)