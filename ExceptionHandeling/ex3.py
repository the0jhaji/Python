class insufficientBalanceError(Exception):
    def __init__(self, accno, cb):
        self.__accno = accno
        self.__curbal = cb
    
    def get_details(self):
        return {'Acc no': self.__accno, 'Current Balance': self.__curbal}


class Customers:
    def __init__(self):
        self.__dct = {}

    def append(self, accno, n, bal):
        self.__dct[accno] = {'Name': n, 'Balance': bal}

    def deposite(self, accno, amt):
        d = self.__dct[accno]
        d['Balance'] += amt

    def display(self):
        for k, v in self.__dct.items():
            print(k, v)
        print()

    def withdraw(self, accno, amt):
        d = self.__dct[accno]
        curbal = d['Balance']
        if curbal - amt < 5000:
            raise insufficientBalanceError(accno, curbal)
        else:
            d['Balance'] -= amt


c = Customers()
c.append(123, 'Sanjay', 9000)
c.append(101, 'Anjay', 8000)
c.append(423, 'Sameer', 7000)
c.append(133, 'Sanket', 9000)

c.deposite(123, 1000)
c.deposite(423, 2000)

c.display()

try:
    c.withdraw(423, 3000)
    print("Amount withdrawn successfully")
    c.display()

    c.withdraw(101, 5000)
    print("Amount withdrawn successfully")
    c.display()

except insufficientBalanceError as ibe:
    print("Withdrawal denied")
    print("Insufficient balance")
    print(ibe.get_details())