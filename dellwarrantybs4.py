#!/usr/bin/python
import sys #module used to receive command line arguments into script and check python version
import requests #module used to request Dell webpage
from bs4 import BeautifulSoup

def getwarranty(servicetag):
    
    """ (str) -> str
    Returns date as string by downloading html as a string and using BeautifulSoup to pull the dates out.
    to find the date. 
    >>> getwarranty('2M95GR1')
    '4/16/2014'
    >>> getwarranty('BKTR3G1')
    '4/22/2011'
    >>> getwarranty('GWQN141')
    '12/18/2006'
    """
    
    r = requests.get("http://www.dell.com/support/troubleshooting/us/en/555/servicetag/" + servicetag + \
        "#ui-tabs-5")
    soup = BeautifulSoup(r.text)
    lis = soup.find_all('li', {"class":'TopTwoWarrantyListItem'})
    warranty = max([li.find_all('b')[1].get_text() for li in lis])
    return warranty

def main():
    args = sys.argv[-1] # Get last word from commandline so it can be checked to see if it's a service tag.
    if not args:
        print('usage: dellwarranty.py [servicetag]')
        sys.exit(1)
    if 'dellwarrantybs4.py' in args:
       print('usage: dellwarranty.py [servicetag]')
       sys.exit(1)
    else:
        servicetag = sys.argv[-1]
        warrantyexpiration = getwarranty(servicetag)
        if warrantyexpiration == "":
            print("Service tag", servicetag, "not found.")
        else:
            print(warrantyexpiration)

if __name__ == '__main__':
    main()
