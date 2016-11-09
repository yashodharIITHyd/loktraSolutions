'''
    ReadMe:
Run the program and it will be the infinite loop
Press 1 for Query_1 as mentioned in the question and the same thing for query 2 also.

For query 1:
    The result will be printed for each page and it will run for the last page

For query 2:
    The result will be printed for required page

Note : If there is no results then it will prints No Result
'''
from bs4 import BeautifulSoup
import requests
website="http://www.shopping.com/"

def getProductsList(queryString):
    data=requests.get(queryString)
    soup=BeautifulSoup(data.text,'lxml')
    results=soup.find("div",id="searchResultsContainer")
    if results==None:
        return None
    else:
        results=results.findAll("div", { "class" : "gridBox" })
        return results

def checkKeyword(keyword):
    keywordList=keyword.split(" ")
    result=""
    l1=len(keywordList)
    i=0
    while i<l1-1:
        result+=keywordList[i]+"+"
        i+=1
    result+=keywordList[i]
    return result

while 1:
    print 'Press 1 for Query_1\nPress 2 for Query_2\n'
    queryNumber=int(raw_input())
    if queryNumber==1:
        keyword=checkKeyword(raw_input('Enter the keyword :'))
        pageNumber=1
        flag=False
        while 1:
            queryString=website+"products~PG-"+str(pageNumber)+"?KW="+keyword
            result=getProductsList(queryString)
            if result==None:
                break
            else:
                flag=True
                print queryString
                for e in result:
                    print e.prettify()
                pageNumber+=1
        if flag==False:
            print 'No Result'

    elif queryNumber==2:
        keyword=checkKeyword(raw_input('Enter the keyword :'))
        pageNumber=int(raw_input("Enter the pageNumber : "))
        queryString=website+"products~PG-"+str(pageNumber)+"?KW="+keyword
        result=getProductsList(queryString)
        if result==None:
            print 'No Result'
        else:
            print queryString
            for e in result:
                print e.prettify()
    else:
        print 'Please enter 1 or 2'
