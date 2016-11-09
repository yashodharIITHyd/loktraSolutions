'''
    Read Me:
Initially create a class file of hashModule and
run the function getString with arguments
of the function are value of the string and
the length of the string
 The required string will be printed.
'''
class hashModule:
    def __init__(self):
        self.letters="acdegilmnoprstuw"

    def getString(self,n,l):    # n is given number and l is length of the string
        result=[None for _ in range(l)]
        count=0
        n-=7*(37**l)
        while count<l:
            result[count]=n%37
            n-=result[count]
            n/=37
            count+=1
        print ''.join(self.letters[e] for e in result[::-1])

h1=hashModule()
h1.getString(680131659347,7)
