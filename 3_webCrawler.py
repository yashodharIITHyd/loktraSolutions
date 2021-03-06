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
from pprint import pprint
import requests
website="http://www.shopping.com/"

def getProductsList(queryString):
    data=requests.get(queryString)
    soup=BeautifulSoup(data.text,'lxml')
    results=soup.find("div",id="searchResultsContainer")
    if results==None:
        return None
    else:
        results=len(results.findAll("div", { "class" : "gridBox" }))
        return results

def getStructuredData(queryString):
    data=requests.get(queryString)
    soup=BeautifulSoup(data.text,'lxml')
    results=soup.find("div",id="searchResultsContainer")
    if results==None:
        return None
    else:
        #results2=results.findAll("div", { "class" : "gridBox" })
        tracks = results.find_all('div', {'class':"gridBox"})
        res={}
        count=1
        for track in tracks:
            discount=track.find("div",{"class":"onSaleTriangle"})
            if discount:
                discount=str(discount.text).strip()
            else:
                discount="No discount"
            title=track.find("h2")
            #print title.text
            if title:
                title2=title.text.encode("utf-8").strip()
            else:
                title2="No title"
            price=track.find("span",{"class":"productPrice"})
            if price:
                price=str(price.text).strip()
            else:
                price="Price is not displayed"
            res.update({
                count:{
                    "discount":discount,
                    "name":title2,
                    "price":price
                }
            })
            count+=1
        return res
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
    print '\n\nPress 1 for Query_1\nPress 2 for Query_2\n'
    queryNumber=int(raw_input())
    if queryNumber==1:
        keyword=checkKeyword(raw_input('Enter the keyword :'))
        pageNumber=1
        flag=False
        noOfItems=0
        while 1:
            queryString=website+"products~PG-"+str(pageNumber)+"?KW="+keyword
            result=getProductsList(queryString)
            if result==None:
                break
            else:
                flag=True
                print queryString,'-->',result
                '''
                for e in result:
                    print e.prettify()
                '''
                noOfItems+=result
                pageNumber+=1
        if flag==False:
            print 'No Result'
        else:
            print 'No of Items : ',noOfItems

    elif queryNumber==2:
        keyword=checkKeyword(raw_input('Enter the keyword :'))
        pageNumber=int(raw_input("Enter the pageNumber : "))
        queryString=website+"products~PG-"+str(pageNumber)+"?KW="+keyword
        result=getStructuredData(queryString)
        if result==None:
            print 'No Result'
        else:
            print queryString
            for product in result.keys():
                print "Name :",result[product]["name"]
                print "Price :",result[product]["price"]
                print "discount :",result[product]["discount"]
                print '\n\n'
    else:
        print 'Please enter 1 or 2'
