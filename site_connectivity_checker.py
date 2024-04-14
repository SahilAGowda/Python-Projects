#import urllib
#use the urllib.request to get the data from the url
#write a function that takes a url 
#return a response 

import urllib.request as urllib


def main(url):
    url=url
    print("Checking Connectivity")
    response = urllib.urlopen(url)
    print("Connected to the",url," Successfully")
    print("The Response of the Code was:",response.getcode())
    
    
    
print("This is a site Connectivity Checker Program")
input_url=input("Input the url of the site you want to check")
main(input_url)