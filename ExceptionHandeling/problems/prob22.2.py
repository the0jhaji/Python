class stack:
    def __init__(self, sz):
        self.size=sz
        self.arr=[]
        self.top=-1

    def push(self, n):
        if self.top +1==self.size:
            raise IndexError("Stack is full")
        else:
            self.top +=1
            self.arr=self.arr+[n]
    def pop(self):
        if self.top==-1:
            raise IndexError ("stack is empty")
        else:
            n=self.arr[self.top]
            self.top-=1
            return n
    def printall(self):
        print(self)
    
s=stack(5)

try:
    s.push(10)
    s.push(30)
    s.push(13)
    s.push(2)
    s.push(1)
    
    n=s.pop()
    print(n)

    s.printall()
except IndexError as ie:
    print(ie.args)