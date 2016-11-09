'''
   ReadMe:
Here input is URL and run the program it will give the list of scheme,netloc,path,port,query
'''
import re
#url="www.shopping.com:12/shoes/products?CLT=SCH"
url=raw_input()

class URL:
    def __init__(self,url):
        self.scheme=''
        self.netloc=''
        self.path=''
        self.port=None
        self.query=''
        l1=None
        path=None
        if '://' in url:
            l1=url.split('://')
        elif '//' in url:
            l1=url.split('//')
        elif ':///' in url:
            l1=url.split(':///')
        elif 7<=len(url) and 'mailto:'==url[:7]:
            l1=['mailto',url[7:]]
        if l1!=None:
            self.scheme=l1[0]
            i=0
            while i<len(l1[1]) and l1[1][i]!='/':
                self.netloc+=l1[1][i]
                i+=1
            path=l1[1][i:]
        else:
            i=0
            while i<len(url) and url[i]!='/':
                self.netloc+=url[i]
                i+=1
            path=url[i:]

        if ':' in self.netloc:
            self.port=self.netloc.split(':')[1]

        if '?' in path:
            self.path=path.split('?')[0]
            self.query=path.split('?')[1]
        else:
            self.path=path

    def scheme(self):
        return self.scheme

    def path(self):
        return self.path

    def netloc(self):
        return self.netloc

    def port(self):
        return self.port

u1=URL(url)
print 'scheme : ',u1.scheme
print 'netloc : ',u1.netloc
print 'path : ',u1.path
print 'port : ',u1.port
print 'query : ',u1.query
